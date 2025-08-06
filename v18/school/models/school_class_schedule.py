# -*- coding: utf-8 -*-

from odoo import fields, models, api
from odoo.exceptions import ValidationError


class ClassSchedule(models.Model):
    _name = "school.class.schedule"
    _inherit = ["soft.delete.mixin",]
    # _description = "Class Creation"

    teacher_id = fields.Many2one("school.teacher", string="Teacher", required=True)
    subject_id = fields.Many2one("school.subject", string="Subject", required=True)
    classroom_id = fields.Many2one("school.classroom", string="Classroom", required=True)

    start_time = fields.Datetime(string="Start Time", required=True)
    end_time = fields.Datetime(string="End Time", required=True)

    name=fields.Char(string="Schedule Name", compute="_compute_name", store=True)

    @api.depends("teacher_id", "classroom_id", "subject_id")
    def _compute_name(self):
        for rec in self:
            rec.name = f"{rec.teacher_id.full_name or 'Teacher'} - {rec.classroom_id.name}"

    @api.onchange("teacher_id")
    @api.depends("teacher_id.subject_ids")
    def _onchange_teacher_id(self):
        if self.teacher_id:
            # if self.subject_id and self.subject_id not in self.teacher_id.subject_ids:
            #     self.subject_id = False  # Clear invalid subject
            return {
                "domain": {
                    "subject_id": [("id", "in", self.teacher_id.subject_ids)]
                }
            }
        else:
            self.subject_id = False
            return {
                "domain": {
                    "subject_id": []
                }
            }

    @api.constrains('start_time', 'end_time')
    def _check_time_range(self):
        for rec in self:
            if rec.start_time and rec.end_time and rec.start_time >= rec.end_time:
                raise ValidationError("End time must be after start time.")

