# -*- coding:utf-8 -*-

from odoo import models, fields,api

class LibraryBookCategory(models.Model):
    _name = "library.book.category"
    _inherit = "soft.delete.mixin"
    _description = "Library Book Category"
    _rec_name = "name"
    _order = "name asc"

    name = fields.Char(string="Category Name", required=True)
    category_id = fields.Char(string="Category ID", readonly=True, copy=False, index=True, default="New")

    @api.model
    def create(self, vals):
        for val in vals:
            if val.get("category_id", "New") == "New":
                val["category_id"] = self.env["ir.sequence"].next_by_code("library.book.category_id") or "New"
        return super(LibraryBookCategory, self).create(vals)