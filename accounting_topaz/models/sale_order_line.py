from odoo import api, fields, models


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'
    z_package_barcode=fields.Char('Full Barcode')

