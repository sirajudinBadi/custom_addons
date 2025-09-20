# -*- coding: utf-8 -*-
##############################################################################
#                                                                            #
# Part of Caret IT Solutions Pvt. Ltd. (Website: www.caretit.com).           #
# See LICENSE file for full copyright and licensing details.                 #
#                                                                            #
##############################################################################
{
    'name': 'Custom Web Snippets',
    'summary': 'Adds custom web snippets',
    'description': '''Module aims to add custom web snippets for Odoo Web Editor drag and drop.''',
    'version': '18.0',
    'author': 'Caret It Solutions PVT. LTD.',
    'category': 'Website',
    'website': 'https://caretit.com',
    'depends': ["base", "website"],
    'data': [
        'security/ir.model.access.csv',
        'views/product_catalog_menus_actions.xml',
        "views/snippets.xml",
        'views/product_catalog_views.xml',
        "views/product_catalog_template.xml"
    ],
    'license': 'LGPL-3',
    'application': True,
    'installable': True,
    'images': ['static/description/icon.png'],
    'assets' : {
        "web.assets_frontend" : [
            "web_snippets/static/src/js/*.js",
            "web_snippets/static/src/css/*.css",
        ],
    }
}
