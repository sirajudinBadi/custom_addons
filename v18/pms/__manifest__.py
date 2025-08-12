{
    "name": "Project Management System",
    "description": "Module to handle all the project related Operations.",
    "summary": """From team to tasks everything is covered under this module.""",
    "version": "18.0.1.1",
    "license": "LGPL-3",
    "author": "John Doe",
    "website": "www.example.com",
    "depends": ["base", "account", "hr"],
    "application": True,
    "installable": True,
    "data": [
        "security/ir.model.access.csv",
        "views/project_actions.xml",
        "views/project_team_member_menus.xml",
        "views/project_team_member_views.xml"
    ],
    "demo" : [
        "demo/project_city_demo_data.xml"
    ],
    "images": ["static/description/icon.png"],
    "sequence": 1,
    'assets': {
        'web.assets_backend': [
            'school/static/src/css/styles.css',
        ],
    }
}
