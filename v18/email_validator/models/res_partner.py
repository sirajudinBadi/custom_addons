# -*-coding:utf-8-*-

from odoo import models, fields, api
import re
from odoo.exceptions import ValidationError

class Partner(models.Model):
    _inherit = 'res.partner'

    _sql_constraints = [
        ("unique_email", "unique(email)", "This email already exist.")
    ]

    @api.constrains('email')
    def _check_email(self):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        for rec in self:
            if rec.email and not re.match(pattern, rec.email):
                raise ValidationError("Please enter a valid email address.")
