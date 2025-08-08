# -*- coding:utf-8 -*-
from email.policy import default

from library.models.library_member import STATUS_SELECTION
from odoo import fields, models, api

FINE_STATUS_SELECTION = [
    ("paid", "Paid"),
    ("unpaid", "Unpaid")
]

class Fine(models.Model):
    _name = "library.fine"
    _inherit = "soft.delete.mixin"

    member_id = fields.Many2one("library.member", string="Member", required=True)
    borrow_id = fields.Many2one("library.borrow", string="Borrow ID")
    fine_amount = fields.Float(string="Fine Amount", required=True)
    status = fields.Selection(selection=FINE_STATUS_SELECTION, default="unpaid")


