{
    "name": "Customer Quick Info",
    "description": "Get quick information about the customers.",
    "website": "www.caretit.com",
    "author": "John Doe",
    "depends": ["base"],
    "data": [
        "views/res_partner_views.xml",
    ],
    "installable": True,
    "application": True,
    'license': 'LGPL-3',
    'images': ['static/description/icon.png'],
    "assets": {
        "web.assets_backend": [
            # ✅ Bootstrap & Font Awesome
            "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css",
            "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js",
            'https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.1/font/bootstrap-icons.css',
            "https://cdn.jsdelivr.net/npm/bootstrap@4.1.3/dist/css/bootstrap.min.css",
            "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css",

            # Owl JS & XML files
            "owl_customer_quick_info/static/src/js/*.js",
            "owl_customer_quick_info/static/src/xml/*.xml",
        ],
    },
}
