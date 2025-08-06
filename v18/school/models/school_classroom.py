# -*- coding : utf-8 -*-

from odoo import fields, models, api


class Classroom(models.Model):
    _name = "school.classroom"
    _inherit = ['soft.delete.mixin']
    _description = "Classroom"
    _order = "name asc"
    # _rec_name = "name"  # WON'T NEED BECAUSE THERE IS ALREADY name FIELD

    name=fields.Char(string="Class Name", required=True)
    location = fields.Char(string="Classroom Location", required=True)

    active = fields.Boolean(string="Active", default=True)


    cls_teacher_id = fields.Many2one(
        "school.teacher",
        string="Class Teacher",
        ondelete = "set null"
    )

    teacher_ids = fields.Many2many(
        'school.teacher',
        "classroom_teacher_rel",
        "classroom_id",
        "teacher_id",
        string='Teachers'
    )

    subject_ids = fields.Many2many(
        "school.subject",
        "subject_classroom_rel",
        "classroom_id",
        "subject_id",
        string="Subjects"
    )

    _sql_constraints = [
        ("unique_name", 'unique(name)', "Class Name must be unique."),
        ("unique_class_teacher", 'unique(cls_teacher_id)', "Only one class teacher per class"),
    ]
