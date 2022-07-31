from odoo import api, fields, models


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'
    # z_package_barcode=fields.Char('Full Barcode')
    product_tmpl_id = fields.Many2one('product.template', 'Product Template', related='product_id.product_tmpl_id')
    z_package_barcode = fields.Char('Full Barcode', related='product_tmpl_id.z_package_barcode')





