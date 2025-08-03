# -*- coding:utf-8 -*-

from odoo import fields, models, api

class Subject(models.Model):
    _name = "school.subject"
    _description = "Subjects"
    _inherit = ["soft.delete.mixin"]

    name = fields.Char(string="Subject Name", required=True)
    code = fields.Char(string="Subject Code", required=True)

    classroom_ids = fields.Many2many(
        "school.classroom",
        "subject_classroom_rel",
        "subject_id",
        "classroom_id",
        string="Classrooms",
    )

    teacher_ids = fields.Many2many(
        "school.teacher",  # Target model
        "teacher_subject_rel",  # Same relation table
        "subject_id",  # This model's column (Subject)
        "teacher_id",  # Target model's column (Teacher)
        string="Teachers"
    )

    _sql_constraints = [
        ("unique_code", 'unique(code)', "Subject code must be unique."),
    ]