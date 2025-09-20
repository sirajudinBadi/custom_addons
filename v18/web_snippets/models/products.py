# -*- coding: utf-8 -*-
##############################################################################
#                                                                            #
# Part of Caret IT Solutions Pvt. Ltd. (Website: www.caretit.com).           #
# See LICENSE file for full copyright and licensing details.                 #
#                                                                            #
##############################################################################

from odoo import models, fields

class ProductCatalog(models.Model):
    _name = "product.catalog"
    _description = "Web Product Catalog Snippet"

    name = fields.Char("Product Name")
    image = fields.Binary("Product Image")
    currency_id = fields.Many2one("res.currency", string="Currency", default=lambda self: self.env.company.currency_id)
    mrp = fields.Monetary("MRP", currency_field="currency_id")
    selling_price = fields.Monetary("Selling Price", currency_field="currency_id")
    rating = fields.Char("Ratings")
    tag = fields.Char("Tag")
    tag_color = fields.Selection(string="Tag Color", selection=[("#F9D018" , "Yellow"), ("#693382" , "Blue"), ("#F3314E" , "Red")])
    text_color = fields.Selection([("#000000", "Black"), ("#FFFFFF", "White")], "Text Color", default="#000000")
    delivery = fields.Selection(string="Delivery Day", selection=[("Today", "Today"), ("Tomorrow", "Tomorrow")])
