# -*-coding:utf-8-*-

from odoo import models,fields,api

class StartEndMixin(models.AbstractModel):
    _name = "startend.mixin"

    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")

