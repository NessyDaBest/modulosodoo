# -*- coding: utf-8 -*-
{
    'name': "libreria_nestor",

    'summary': "Short (1 phrase/line) summary of the module's purpose",
    'license': "AGPL-3",
    'description': """
    Modulo de odoo sobre una libreria creado con scaffolding y sincronizado con GitHub
    """,

    'author': "Néstor Montoro Molina",
    'website': "https://github.com/NessyDaBest/modulosodoo",
    'category': 'Tools',
    'version': '1.0',

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base' , 'contacts'],

    # always loaded
    'data': [
        'security/libreria_security.xml',
        'security/ir.model.access.csv',
        'views/libreria.xml',
        #'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
    'installable': True,
}

