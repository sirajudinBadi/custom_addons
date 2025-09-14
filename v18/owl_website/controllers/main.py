# -*-coding:utf-8-*-

from odoo import http
from odoo.http import request

class Main(http.Controller):
    @http.route("/owl_website/objects", type="http", auth="public")
    def list(self, **kwargs):
        return request.render(
            "owl_website.listing",
            {
                "root" : "/owl_website",
                "objects" : request.env["main"].search([])
            }
        )