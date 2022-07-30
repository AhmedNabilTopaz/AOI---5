# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models



class StockMove(models.Model):
    _inherit = "stock.move"
    z_package_barcode=fields.Char('Full Barcode')
