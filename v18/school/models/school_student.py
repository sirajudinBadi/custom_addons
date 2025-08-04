# -*- coding: utf-8 -*-
import typing

from odoo import fields, models, api

GENDER_SELECTION = [
    ("male", "Male"),
    ("female", "Female"),
    ("other", "Other")
]

class Student(models.Model):
    _name = "school.student"
    _description = "Student"
    _inherit = ['soft.delete.mixin']
    _order = "enrollment_id asc"

    enrollment_id = fields.Char(string="Enrollment ID", index=True, copy=False, readonly=True, default="New")
    first_name = fields.Char(string="First Name", required=True)
    last_name = fields.Char(string="Last Name", required=True)
    gender = fields.Selection(selection=GENDER_SELECTION, required=True, string="Gender")
    birth_date = fields.Date(string="Date of Birth", required=True)
    email = fields.Char(string="Email-ID", required=True)
    mobile = fields.Char(string="Mobile No.", required=True)
    admission_date = fields.Date(string="Admission Date", readonly=True, default=fields.Date.today)

    current_address = fields.Text(string="Current Address", required=True)
    permanent_address = fields.Text(string="Permanent Address")
    same_as_current = fields.Boolean(string="Same As Current Address", default=False)

    classroom_id = fields.Many2one("school.classroom", string="Classroom")
    is_monitor = fields.Boolean(string="Monitor", default= False)
    active = fields.Boolean(string="Active", default=True)

    father_name = fields.Char(string="Father Name")
    father_occupation = fields.Char(string="Father Occupation")
    mother_name = fields.Char(string="Mother Name")
    mother_occupation = fields.Char(string="Mother Occupation")

    parent_mobile = fields.Char(string="Parent Mobile")
    parent_email = fields.Char(string="Parent Email")

    _sql_constraints = [
        ("unique_enrollment_id", 'unique(enrollment_id)', "Enrollment ID must be unique."),
        ("unique_student_email", 'unique(email)', "Student Email must be unique."),
        ("unique_student_mobile", 'unique(mobile)', "Student mobile no. must be unique."),
        ("unique_parent_email", 'unique(parent_email)', "Parent Email must be unique."),
        ("unique_parent_mobile", 'unique(parent_mobile)', "Parent mobile no. must be unique."),
    ]

    @api.model
    def create(self, vals):
        if vals.get("enrollment_id", "New") == "New":
            vals["enrollment_id"] = self.env["ir.sequence"].next_by_code("student.enrollment") or "New"
        return super(Student, self).create(vals)

    def name_get(self):
        result = []
        for rec in self:
            name = f"{rec.enrollment_id}-{rec.first_name} {rec.last_name}"
            result.append((rec.id, name))
        return result









