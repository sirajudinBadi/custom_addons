# -*- coding: utf-8 -*-
{
    'name': 'Cybro Web',
    'depends': [
        'base', 'website',
    ],
    'data': [
            'views/snippets/snippet_template.xml'
    ],
    'assets': {
        'web.assets_frontend': [
            'owl_web_cybro/static/src/js/*',
            'owl_web_cybro/static/src/xml/*'
        ]
    },
}
