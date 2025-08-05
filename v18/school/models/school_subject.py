# -*- coding:utf-8 -*-

from odoo import fields, models, api

class Subject(models.Model):
    _name = "school.subject"
    _description = "Subjects"
    _inherit = ["soft.delete.mixin"]
    _order = "name asc"
    # Here too _rec_name will not be needed bcz there is already name field in the model

    name = fields.Char(string="Subject Name", required=True)
    code = fields.Char(string="Subject Code", readonly=True, copy=False, index=True, default="New")

    active = fields.Boolean(string="Active", default=True)

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

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get("code", "New") == "New" and vals.get("name"):
                subject = vals.get("name")

                prefix_parts = []
                if " " in subject:
                    words = subject.strip().split()
                    for word in words:
                        if word.lower() == "and" or word == "&":
                            prefix_parts.append("&")
                        else:
                            prefix_parts.append(word[0].upper())
                else:
                    prefix_parts.append(subject.upper())
                prefix = "".join(prefix_parts)
                seq_num = self.env["ir.sequence"].next_by_code("subject.code") or "00"
                vals["code"] = f"{prefix}-{seq_num}"

        return super(Subject, self).create(vals_list)