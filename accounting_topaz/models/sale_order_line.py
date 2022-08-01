from odoo import api, fields, models


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'
    # product_tmpl_id = fields.Many2one('product.template', 'Product Template', related='product_id.product_tmpl_id')
    z_package_barcode = fields.Char('Full Barcode', related='product_template_id.z_package_barcode')




