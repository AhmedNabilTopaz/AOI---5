# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, tools


class ReportStockQuantity(models.Model):
    _inherit = 'report.stock.quantity'
    z_package_barcode = fields.Char('Full Barcode', compute='_getdata', store=True)

    def _getdata(self):
        sql = """select z_package_barcode from product_template where id=%s"""
        self.env.cr.execute(sql, self.product_tmpl_id)
        for rec in self.env.cr.fetchall():
            self.z_package_barcode = rec[0]
            print("Name is", rec[0])