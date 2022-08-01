# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models



class StockMove(models.Model):
    _inherit = "stock.move"
    product_tmpl_id = fields.Many2one('product.template', 'Product Template', related='product_id.product_tmpl_id')
    z_package_barcode = fields.Char('Full Barcode', related='product_tmpl_id.z_package_barcode')


