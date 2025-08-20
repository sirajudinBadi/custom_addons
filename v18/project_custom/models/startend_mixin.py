# -*-coding:utf-8-*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class StartEndMixin(models.AbstractModel):
    _name = "startend.mixin"
    _description = "Start End Mixin"
    _abstract = True

    date_start = fields.Datetime("Start Date", index=True, copy=False)
    date_end = fields.Datetime("End Date", index=True, copy=False)

    @api.constrains("date_start", "date_end")
    def validate_dates(self):
        for rec in self:
            if rec.date_start and rec.date_end and rec.date_start > rec.date_end:
                raise ValidationError("Start Date must be before End Date")
