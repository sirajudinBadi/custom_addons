# -*- coding:utf-8 -*-

from odoo import fields, models, api

class Book(models.Model):
    _name = "library.book"
    _inherit = "soft.delete.mixin"
    _description = "Library Book"
    _order = ""
    _rec_name = ""

    isbn = fields.Char(string="ISBN", readonly=True, copy=False)
    name = fields.Char(string="Title", required=True, index=True)
    category_id = fields.Many2one("library.category", string="Category", required=True)
    author_ids = fields.Many2many("library.author", "book_author_rel", "book_id", "author_id", "Authors")
    borrow_ids = fields.One2many("library.borrow", "book_id", "Borrowers")
    total_copies = fields.Integer(string="Total Copies", default=1)
    available_copies = fields.Integer(compute="_compute_available_copies", store=True)

    def _compute_available_copies(self):
        for book in self:
            borrowed= self.env["library.borrow"].search_count([
                ("book_id", "=", book.id),
                ("status", "=", "borrowed")
            ])
            book.available_copies = book.total_copies - borrowed