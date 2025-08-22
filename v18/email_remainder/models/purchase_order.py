# -*-coding:utf-8-*-

from odoo import models, fields

class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    state = fields.Selection(selection_add=[
        ("first_approval", "First Approval"),
        ("second_approval", "Second Approval"),
    ])

    def button_confirm(self):
        if self.partner_id.credit_limit > float(
            self.env["ir.config_parameter"].sudo().get_param("res_partner.credit_limit", 0.0)
        ):
            self.write({"state" : "first_approval"})
        return super(PurchaseOrder,self).button_confirm()