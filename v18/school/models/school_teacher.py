# -*- coding: utf-8 -*-

from odoo import fields, models, api

class Teacher(models.Model):
    _name = "school.teacher"
    _description = "Teacher"
    _inherit = ["soft.delete.mixin",]

    first_name = fields.Char(string="First Name", required=True)
    last_name = fields.Char(string="Last Name", required=True)
    join_date = fields.Date(string="Join Date", readonly=True , default=fields.Date.today)

    is_class_teacher= fields.Boolean(string="Class Teacher", default=True)
    # For class teacher purpose
    classroom_id = fields.Many2one(
        "school.classroom",
        string="Assigned Class",
        ondelete = "set null",
    )

    # For teaching purpose
    classroom_ids = fields.Many2many(
        'school.classroom',
        "classroom_teacher_rel",
        "teacher_id",
        "classroom_id",
        string="Classrooms"
    )

    subject_ids = fields.Many2many(
        "school.subject",  # Target model
        "teacher_subject_rel",  # Relation table name
        "teacher_id",  # This model's column (Teacher)
        "subject_id",  # Target model's column (Subject)
        string="Subjects"
    )