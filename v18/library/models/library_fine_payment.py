# -*-coding:utf-8-*-

from odoo import fields, models, api


class FinePayment(models.Model):
    _name = "library.fine.payment"
    _inherit = "soft.delete.mixin"

    member_id = fields.Many2one("library.member", "Member")
    fine_id = fields.Many2one("library.fine", string="Fine ID")

    payment_date = fields.Date(string="Payment Date", default=fields.Date.today)
    payment_amount = fields.Float(string="Amount Paid")

    def switch_payment_status(self):
        for rec in self:
            if rec.fine_id and rec.payment_amount >= rec.fine_id.fine_amount:
                rec.fine_id.write({
                    "status" : "paid",
                    "fine_amount" : 0.0
                })
