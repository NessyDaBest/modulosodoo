# -*- coding: utf-8 -*-
{
    'name': "videoclub_nestor",

    'summary': "Short (1 phrase/line) summary of the module's purpose",
    'license': "AGPL-3",
    'description': """
    Modulo de odoo sobre un videoclub creado con scaffolding y sincronizado con GitHub
    """,

    'author': "Néstor Montoro Molina",
    'website': "https://github.com/NessyDaBest/modulosodoo",
    'category': 'Tools',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        #'security/ir.model.access.csv',
        'views/videoclub.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
    'installable': True,
}

