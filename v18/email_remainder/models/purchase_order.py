# -*-coding:utf-8-*-

from odoo import models, fields

class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    state = fields.Selection(selection_add=[
        ("first_approval", "First Approval"),
        ("second_approval", "Second Approval"),
    ])