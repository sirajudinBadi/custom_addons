# -*- coding: utf-8 -*-

from odoo import fields, models, api

GROUP_SELECTION = [
    ("primary", "Primary"),
    ("secondary", "Secondary")
]

GENDER_SELECTION = [
    ("male", "Male"),
    ("female", "Female"),
    ("other", "Other")
]


class Teacher(models.Model):
    _name = "school.teacher"
    _description = "Teacher"
    _inherit = ["soft.delete.mixin", ]
    _rec_name = 'full_name'

    employment_id = fields.Char(string="Employment ID", readonly=True, index=True, copy=False, default="New")
    first_name = fields.Char(string="First Name", required=True)
    last_name = fields.Char(string="Last Name", required=True)
    gender = fields.Selection(selection=GENDER_SELECTION, string="Gender")
    join_date = fields.Date(string="Join Date", readonly=True, default=fields.Date.today)
    image_128 = fields.Image(string="Profile Picture")

    schedule_ids = fields.Many2one("school.teacher.schedule", string="Schedule")

    full_name = fields.Char(string="Full Name", compute="_computed_full_name", search="_search_full_name", store=True)

    active = fields.Boolean(string="Active", default=True)

    group = fields.Selection(selection = GROUP_SELECTION,default= "primary", string="Group", compute="_compute_group", store=True)

    # is_class_teacher = fields.Boolean(string="Class Teacher", default=True)
    # For class teacher purpose
    classroom_id = fields.Many2one(
        "school.classroom",
        string="Class Teacher",
        ondelete="set null",
    )

    # For teaching purpose
    classroom_ids = fields.Many2many(
        'school.classroom',
        "classroom_teacher_rel",
        "teacher_id",
        "classroom_id",
        string="Classrooms"
    )

    primary_subject = fields.Many2one(
        "school.subject",
        string = "Subject",
        ondeleted="set null",
    )

    subject_ids = fields.Many2many(
        "school.subject",  # Target model
        "teacher_subject_rel",  # Relation table name
        "teacher_id",  # This model's column (Teacher)
        "subject_id",  # Target model's column (Subject)
        string="Subjects"
    )

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get("employment_id", "New") == "New":
                vals["employment_id"] = self.env["ir.sequence"].next_by_code("teacher.employment") or "New"
        return super(Teacher, self).create(vals_list)

    def name_get(self):
        result = []
        for rec in self:
            name = f"{rec.employment_id}-{rec.first_name} {rec.last_name}"
            result.append((rec.id, name))
        return result

    @api.depends("first_name", "last_name")
    def _computed_full_name(self):
        for rec in self:
            rec.full_name = f"{rec.first_name} {rec.last_name}"

    @api.model
    def _search_full_name(self, operator, value):
        return [
            "|",
            ("first_name", operator, value),
            ("last_name", operator, value)
        ]

    @api.depends("classroom_ids")
    def _compute_group(self):
        for rec in self:
            rec.group = "secondary"
            for cls in rec.classroom_ids:
                if cls.name:
                    prefix = cls.name.split("-")[0]
                    if prefix.isdigit() and 1 <= int(prefix) <= 4:
                        rec.group = "primary"
                        break


