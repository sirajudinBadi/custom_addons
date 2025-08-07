# -*- coding:utf-8 -*-

from odoo import fields, models, api

class TeacherProfile(models.Model):
    _name="school.teacher.profile"
    _inherits = {"res.partner" : "partner_id"}

    partner_id = fields.Many2one("res.partner", required=True, ondelete="cascade")

    teacher_id = fields.Many2one("school.teacher", string="Teacher", required=True)
    password = fields.Char(string="Password", help="Password for profile creation.")
