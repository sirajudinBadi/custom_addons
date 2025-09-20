# -*- coding: utf-8 -*-
##############################################################################
#                                                                            #
# Part of Caret IT Solutions Pvt. Ltd. (Website: www.caretit.com).           #
# See LICENSE file for full copyright and licensing details.                 #
#                                                                            #
##############################################################################
from odoo import http
from odoo.http import request

class ProductCatalog(http.Controller):
    @http.route("/product/catalog", type="json", methods=["POST"], auth="public")
    def get_products(self):
        products = request.env["product.catalog"].sudo().search_read([])
        return products

