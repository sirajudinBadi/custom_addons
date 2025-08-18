# -*-coding:utf-8-*-

from odoo import models,fields,api
from odoo.exceptions import ValidationError


class StartEndMixin(models.AbstractModel):
    _name = "startend.mixin"

    date_start = fields.Date(string="Start Date")
    date_end = fields.Date(string="End Date")

    @api.constrains('date_start', 'date_end')
    def check_dates(self):
        for rec in self:
            if rec.date_start and rec.date_end and  rec.date_start > rec.date_end:
                raise ValidationError("Start date must be before End Date.")
