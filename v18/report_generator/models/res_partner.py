# coding:utf-8-*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class ResPartner(models.Model):
    _inherit = "res.partner"

    def get_customers(self):
        customers = self.env['res.partner'].sudo().search([
            ("customer_rank", '>', 0),
            ("active", '=', True),
        ])

        return customers

    def generate_customer_pdf(self):
        customers = self.get_customers()
        print(f"========================\n{customers}")
        if not customers:
            raise ValidationError("No customers exist.")
        print(self.env.ref("report_generator.report_customer_action").report_action(customers))
        return self.env.ref("report_generator.report_customer_action").report_action(customers)