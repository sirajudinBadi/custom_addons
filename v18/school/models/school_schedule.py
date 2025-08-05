# -*- coding:utf-8 -*-
from email.policy import default

from odoo import fields, api, models

HOLIDAY_TYPES = [
    ("public", "Public"),
    ("event", "Event"),
    ("vacation", "Vacation")
]

COLOR_MAPPING = {
    'public': 1,
    'event': 2,
    'vacation': 3,
}

class Schedule(models.Model):
    _name = "school.schedule"
    _inherit = ["soft.delete.mixin"]
    _description = "Schedule for school"
    _order = "start_date asc"
    _rec_name = "name"

    name = fields.Char(string="Holiday Name")
    start_date = fields.Date(string="Start Date", required=True)
    end_date = fields.Date(string="End Date", required=True)
    holiday_type = fields.Selection(selection=HOLIDAY_TYPES, string="Holiday Type", default="public")
    color_index = fields.Integer(string="Color Index", compute="_compute_color_index")

    @api.depends("holiday_type")
    def _compute_color_index(self):
        for rec in self:
            rec.color_index = COLOR_MAPPING.get(rec.holiday_type, 0)

