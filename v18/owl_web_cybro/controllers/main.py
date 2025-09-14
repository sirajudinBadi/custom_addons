# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class WebsiteSnippetOwl(http.Controller):
    @http.route('/get_product_details', type='json', auth='public', methods=['POST'])
    def get_product_details(self):
        """ Function to get product details for the snippet"""
        return request.env['product.product'].search_read([('image_1920', '!=', False)],
                                                          ['name', 'lst_price', 'default_code', 'image_1920'], limit=8)
