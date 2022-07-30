# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import tools
from odoo import api, fields, models


class SaleReport(models.Model):
    _inherit = "sale.report"
    z_package_barcode = fields.Char('Full Barcode', related='product_tmpl_id.z_package_barcode', store=True)

    def _select_sale(self, fields=None):
        return super(SaleReport,
                     self)._select_sale() + ", t.z_package_barcode as z_package_barcode"

    def _group_by_sale(self, groupby=''):
        return super(SaleReport, self)._group_by_sale() + ", t.z_package_barcode"
