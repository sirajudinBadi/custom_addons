# -*- coding:utf-8 -*-

from odoo import fields, models

class Author(models.Model):
    _name = "library.author"
    _inherit = "soft.delete.mixin"

    image_128 = fields.Image(string="Author's Image")
    first_name = fields.Char(string="First Name", required=True)
    last_name = fields.Char(string="Last Name", required=True)
    book_ids = fields.Many2many("library.book", "book_author_rel", "author_id", "book_id", "Books")
