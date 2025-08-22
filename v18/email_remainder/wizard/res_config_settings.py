# -*-coding:utf-8-*-

from odoo import models, fields

class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    credit_limit = fields.Float(string="Max Credit Limit")
