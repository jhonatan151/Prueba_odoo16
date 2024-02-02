# -*- coding: utf-8 -*-
{
    'name': "agregarcamposfsmorder",

    'summary': """incluir""",

    'description': """
        para crear campos al modulo servicio de campo""",

    'author': "All Service Rhyno",
    'website': "http://allser.com.co",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'custom',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','fieldservice','stock'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/ejecucion_fsm.xml',
        #'views/generate_pdf.xml',
        #'views/report.xml'
    ],
    # only loaded in demonstration mode
    'installable': True,
    'application': False,
    'auto_install': False,
}
