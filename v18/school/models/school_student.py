# -*- coding: utf-8 -*-

from odoo import fields, models, api, _
from dateutil.relativedelta import relativedelta

from odoo.exceptions import ValidationError

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
    _rec_name = "full_name"

    enrollment_id = fields.Char(string="Enrollment ID", index=True, copy=False, readonly=True, default="New")
    image_128 = fields.Image(string="Student Image")
    first_name = fields.Char(string="First Name")
    last_name = fields.Char(string="Last Name")
    gender = fields.Selection(selection=GENDER_SELECTION, required=True, string="Gender")
    birth_date = fields.Date(string="Date of Birth", required=True)
    email = fields.Char(string="Email-ID", required=True)
    mobile = fields.Char(string="Mobile No.", required=True)
    admission_date = fields.Date(string="Admission Date", readonly=True, default=fields.Date.today)

    # class_location = fields.Char(string="Class Location", related="classroom_id.location")

    age = fields.Integer(string="Age", compute="_compute_age", store=True)
    full_name = fields.Char(string="Full Name", compute="_computed_name", inverse="_inverse_fullname", search="_search_full_name", store=True)

    current_address = fields.Text(string="Current Address", required=True)
    permanent_address = fields.Text(string="Permanent Address")
    same_as_current = fields.Boolean(string="Same As Current Address", default=False)

    classroom_id = fields.Many2one("school.classroom", string="Classroom")
    # is_monitor = fields.Boolean(string="Monitor", default=False)
    active = fields.Boolean(string="Active", default=True)

    father_name = fields.Char(string="Father Name")
    father_occupation = fields.Char(string="Father Occupation")
    mother_name = fields.Char(string="Mother Name")
    mother_occupation = fields.Char(string="Mother Occupation")



    parent_mobile = fields.Char(string="Parent Mobile")
    parent_email = fields.Char(string="Parent Email")

    file = fields.Binary(string="File", required=True, help="Only PDF Allowed.")
    file_name = fields.Char(string="File Name", required=True)

    is_verified = fields.Boolean(string="Verification Status", compute = "_compute_verified", store=True)

    _sql_constraints = [
        ("unique_enrollment_id", 'unique(enrollment_id)', "Enrollment ID must be unique."),
        ("unique_student_email", 'unique(email)', "Student Email must be unique."),
        ("unique_student_mobile", 'unique(mobile)', "Student mobile no. must be unique."),
        ("unique_parent_email", 'unique(parent_email)', "Parent Email must be unique."),
        ("unique_parent_mobile", 'unique(parent_mobile)', "Parent mobile no. must be unique."),
    ]

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get("enrollment_id", "New") == "New":
                vals["enrollment_id"] = self.env["ir.sequence"].next_by_code("student.enrollment") or "New"
        return super(Student, self).create(vals_list)

    def name_get(self):
        result = []
        for rec in self:
            name = f"{rec.enrollment_id}-{rec.first_name} {rec.last_name}"
            result.append((rec.id, name))
        return result

    @api.depends("birth_date")
    def _compute_age(self):
        for rec in self:
            rec.age = relativedelta(fields.Date.today(), rec.birth_date).years

    @api.depends("first_name", "last_name", "is_verified")
    def _computed_name(self):
        for rec in self:
            name = f"{rec.first_name} {rec.last_name}".strip()
            if rec.is_verified:
                name += "🔹"
            rec.full_name = name

    @api.model
    def _search_full_name(self, operator, value):
        return [
            "|",
            ("first_name", operator, value),
            ("last_name", operator, value),
        ]

    def _inverse_fullname(self):
        for rec in self:
            if rec.full_name:
                parts= rec.full_name.strip().split(" ", 1)
                rec.first_name = parts[0]
                rec.last_name = parts[1] if len(parts) > 1 else ""

    @api.constrains("file", "file_name")
    def _check_file_type(self):
        for rec in self:
            if rec.file and rec.file_name:
                if not rec.file_name.lower().endswith(".pdf"):
                    raise ValidationError("Only Aadhar PDF is allowed.")

    @api.depends("file")
    def _compute_verified(self):
        for rec in self:
            rec.is_verified = bool(rec.file)

    @api.onchange("same_as_current", "current_address")
    def _onchange_same_as_current(self):
        for rec in self:
            if rec.same_as_current:
                rec.permanent_address = rec.current_address
            else:
                rec.permanent_address = False


    def action_student_complaint(self):
        return {
            "name" : _('Complaint'),
            "view_mode" : "form",
            "res_model" : "school.student.complaint",
            "type" : "ir.actions.act_window",
            "target" : "new"
        }

    def action_open_google(self):
        return {
            "type" : "ir.actions.act_url",
            "url" : "https://www.google.com",
            "target" : "new"
        }

    @api.model
    def permanently_delete_record(self):
        soft_deleted_records = self.search([("active","=", False)])
        if soft_deleted_records:
            soft_deleted_records.unlink()