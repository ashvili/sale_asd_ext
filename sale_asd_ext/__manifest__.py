# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Sale_asd_ext',
    'version': '0.0.1',
    # 'category': 'Sales',
    'depends': [
        'base',
        'sale',
    ],
    'data': [
        # 'security/ir.model.access.csv',
        'views/sale_asd_ext_views.xml',
        'report/ir_actions_report_templates.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}