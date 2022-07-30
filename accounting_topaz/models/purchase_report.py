# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import itertools
import logging
from collections import defaultdict

from odoo import api, fields, models, tools, _, SUPERUSER_ID
from odoo.exceptions import ValidationError, RedirectWarning, UserError
from odoo.osv import expression
import re

_logger = logging.getLogger(__name__)


class PurchaseReport(models.Model):
    _inherit = "purchase.report"
    # z_package_barcode = fields.Char('Full Barcode', related='product_tmpl_id.z_package_barcode', store=True)
    # z_package_barcode= fields.Many2one('product.template','Full Barcode',readonly=True)
    z_package_barcode = fields.Char('Full Barcode', compute='_getdata', store=True)

    def _getdata(self):
        sql = """select z_package_barcode from product_template where id=%s"""
        self.env.cr.execute(sql, self.product_tmpl_id)
        for rec in self.env.cr.fetchall():
            self.z_package_barcode = rec[0]
            print("Name is", rec[0])
    def _select(self):
        return super(PurchaseReport,
                     self)._select() + ", t.z_package_barcode as z_package_barcode"

    # def _from(self):
    #     return super(PurchaseReport, self)._from() + " left join product_template t on (t.z_package_barcode=po.picking_type_id)"

    def _group_by(self):
        return super(PurchaseReport, self)._group_by() + ", t.z_package_barcode"

    @api.model
    def read_group(self, domain, fields, groupby, offset=0, limit=None, orderby=False, lazy=True):
        """ This is a hack to allow us to correctly calculate the average of PO specific date values since
            the normal report query result will duplicate PO values across its PO lines during joins and
            lead to incorrect aggregation values.

            Only the AVG operator is supported for avg_receipt_delay.
        """
        avg_receipt_delay = next((field for field in fields if re.search(r'\bavg_receipt_delay\b', field)), False)

        if avg_receipt_delay:
            fields.remove(avg_receipt_delay)
            if any(field.split(':')[1].split('(')[0] != 'avg' for field in [avg_receipt_delay] if field):
                raise UserError(
                    "Value: 'avg_receipt_delay' should only be used to show an average. If you are seeing this message then it is being accessed incorrectly.")

        res = []
        if fields:
            res = super(PurchaseReport, self).read_group(domain, fields, groupby, offset=offset, limit=limit,
                                                         orderby=orderby, lazy=lazy)

        if not res and avg_receipt_delay:
            res = [{}]

        if avg_receipt_delay:
            query = """ SELECT AVG(receipt_delay.po_receipt_delay)::decimal(16,2) AS avg_receipt_delay
                              FROM (
                                  SELECT extract(epoch from age(po.effective_date, po.date_planned))/(24*60*60) AS po_receipt_delay
                                  FROM purchase_order po
                                  WHERE po.id IN (
                                      SELECT "purchase_report"."order_id" FROM %s WHERE %s)
                                  ) AS receipt_delay
                        """

            subdomain = domain + [('company_id', '=', self.env.company.id), ('effective_date', '!=', False)]
            subtables, subwhere, subparams = expression(subdomain, self).query.get_sql()

            self.env.cr.execute(query % (subtables, subwhere), subparams)
            res[0].update({
                '__count': 1,
                avg_receipt_delay.split(':')[0]: self.env.cr.fetchall()[0][0],
            })
        return res
