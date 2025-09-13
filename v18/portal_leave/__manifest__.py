# -*- coding: utf-8 -*-
##############################################################################
#
# Part of Caret IT Solutions Pvt. Ltd. (Website: www.caretit.com).
# See LICENSE file for full copyright and licensing details.
#
##############################################################################

{
    'name': 'Portal Leave Application',
    'summary': 'Allow portal user to take a leave.',
    'description': '''Module aims to add leave management inside portal user's my account tab.''',
    'version': '10.0',
    'author': 'Caret It Solutions PVT. LTD.',
    # 'category': '',
    'website': 'https://caretit.com',
    'depends': ["base","hr", "hr_holidays",],
    "installable" : True,
    "application" : True,
    'data': [
        # "views/portal_templates.xml",
        "views/leave_list_template.xml",
        "views/create_leave_template.xml",
        "views/portal_leave_template.xml",
    ],
    'license': 'LGPL-3',
    'images': ['static/description/icon.png'],
    "assets": {
            "web.assets_backend": [
                # ✅ Bootstrap & Font Awesome
                "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css",
                "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js",
                'https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.1/font/bootstrap-icons.css',
                "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css",

                # Owl JS & XML files
                # "portal_leave/static/src/js/*.js",
                # "portal_leave/static/src/xml/*.xml",
            ],
        },
}