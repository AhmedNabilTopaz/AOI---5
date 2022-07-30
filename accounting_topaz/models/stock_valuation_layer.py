# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, tools


class StockValuationLayer(models.Model):
    """Stock Valuation Layer"""
    _inherit = 'stock.valuation.layer'
    z_package_barcode=fields.Char('Full Barcode',related='product_tmpl_id.z_package_barcode')
