# -*- coding:utf-8 -*-

from odoo import fields, models, api

class StudentHealth(models.Model):
    _inherit = 'school.student'

    health_score = fields.Float(string="Health Score", help="Score based on report.")
    is_allergen = fields.Boolean(string="Allergies")
