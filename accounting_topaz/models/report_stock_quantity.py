# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, tools


class ReportStockQuantity(models.Model):
    _inherit = 'report.stock.quantity'
    z_package_barcode=fields.Char('Full Barcode',related='product_tmpl_id.z_package_barcode')
