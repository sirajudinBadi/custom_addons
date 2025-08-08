# -*- coding:utf-8 -*-

from odoo import fields, models, api
from odoo.api import depends

ROLE_SELECTION = [
    ("student", "Student"),
    ("teacher", "Teacher"),
]

STATUS_SELECTION = [
    ("active", "Active"),
    ("dormant", "Dormant"),
    ("inactive", "Inactive")
]

class Member(models.Model):
    _name = "library.member"
    _inherit = "soft.delete.mixin"

    first_name = fields.Char(string="First Name", required=True)
    last_name = fields.Char(string="Last Name", required=True)

    join_date = fields.Date(string="Join Date", default=fields.Date.today)
    role = fields.Selection(selection=ROLE_SELECTION, string="Role", required=True)
    status = fields.Selection(selection=STATUS_SELECTION, string="Status", required=True, default="active")

    name = fields.Char(string="Full Name", compute="_compute_full_name", store=True)

    @api.depends("first_name", "last_name")
    def _compute_full_name(self):
        for rec in self:
            rec.name = f"{rec.first_name} {rec.last_name}"
