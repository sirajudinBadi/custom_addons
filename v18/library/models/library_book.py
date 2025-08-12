# -*-coding:utf-8-*-

from odoo import models, fields, api

class LibraryBook(models.Model):
    _name = "library.book"
    _inherit = "soft.delete.mixin"
    _description = "Library Book"
    _rec_name = "name"
    _order = "name asc"

    name = fields.Char(string="Book Name", required=True)
    category = fields.Many2one("library.book.category", string="Category", required=True)
