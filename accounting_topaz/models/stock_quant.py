# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import logging

from psycopg2 import Error, OperationalError

from odoo import _, api, fields, models
from odoo.exceptions import UserError, ValidationError
from odoo.osv import expression
from odoo.tools.float_utils import float_compare, float_is_zero

_logger = logging.getLogger(__name__)


class StockQuant(models.Model):
    _inherit = 'stock.quant'
    z_package_barcode=fields.Char('Full Barcode',related='product_tmpl_id.z_package_barcode')
    # z_package_barcode = fields.Many2one(
    #     'product.template', string='Product Template',
    #     related='product_id.z_package_barcode',
    # auto_join=True, ondelete='restrict', required=True, index=True, check_company=True)

