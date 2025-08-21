# -*-coding:utf-8-*-

from odoo import models,fields,api

class Partner(models.Model):
    _inherit = "res.partner"

    restrict_email = fields.Boolean("Restrict Email", default=False, help="If enabled, partner will not receive emails.")

