# -*- coding: utf-8 -*-
{
    'name': "Retenciones personalizadas Tucuman",

    'summary': """
        Retenciones personalizadas Tucuman""",

    'description': """
        Este modulo permite la configuracion de las retenciones personalizadas de Tucuman, Argentina.
    """,

    'author': "OutsourceArg",
    'website': "https://www.outsourcearg.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ["account","account-payment-group"],
    "data":["views/tucuman.xml",],
    "installable": True,
    #"pre_init_hook": "pre_init_hook",
}