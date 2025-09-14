# -*-coding:utf-8-*-

{
    "name": "Owl Website",
    "version": "18.0.1.0.0",
    "summary": """Website development using Owl JS""",
    "author": "Sirajudin Badi",
    "website": "www.example.com",
    "category": "website",
    "depends": ["base", "web", "website"],
    "data": [
        "views/hello_world_views.xml",
    ],
    "application": True,
    "installable": True,
    "license": "LGPL-3",
    'assets': {
        'web.assets_frontend': [
            'owl_website/static/src/portal_component/**/*',
        ],
    }
}
