# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Topaz Accounting',
    'version': '1.0',
    'summary': 'Editing Accounting ',
    'description': "",
    'website': 'https://www.odoo.com/app/inventory',
    'depends': ['account', 'purchase', 'sale', 'stock'],
    'sequence': -100,
    'data': [
        'views/account_move_views.xml',
        'views/purchase_views.xml',
        'views/sale_views.xml',
        'views/stock_picking_views.xml',
        'views/product_template_views.xml',
        'views/product_views.xml',
        'views/stock_quant_views.xml',
        'views/purchase_report_views.xml',
        'views/stock_valuation_layer_views.xml',
        'views/stock_move_line_views.xml',
        'views/sale_report_views.xml',
        'views/report_deliveryslip.xml',
        'views/report_stock_quantity.xml',
        'report/sale_report_templates.xml'
    ],
    'license': 'LGPL-3'

}
