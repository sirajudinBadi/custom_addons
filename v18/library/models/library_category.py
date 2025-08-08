# -*- coding:utf-8 -*-

from odoo import fields, models

class Category(models.Model):
    _name = "library.category"
    _inherit = "soft.delete.mixin"
    _order = "name"
    _rec_name = "name"

    name = fields.Char(string="Name", required=True, index=True)