# -*-coding:utf-8-*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class StartEndMixin(models.AbstractModel):
    _name = "startend.mixin"
    _description = "Start End Mixin"
    _abstract = True

    date_start = fields.Date("Start Date")
    date_end = fields.Date("End Date")

    @api.constrains("date_start", "date_end")
    def validate_dates(self):
        for rec in self:
            if rec.date_start and rec.date_end and rec.date_start > rec.date_end:
                raise ValidationError("Start Date must be before End Date")
