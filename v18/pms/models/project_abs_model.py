# -*-coding:utf-8-*-

from odoo import models,fields,api

class StartEndMixin(models.AbstractModel):
    _name = "startend.mixin"

    date_start = fields.Date(string="Start Date")
    date_end = fields.Date(string="End Date")

