# -*-coding:utf-8-*-

from odoo import models, fields, api
from odoo.api import ValuesType, Self
from odoo.exceptions import ValidationError, UserError


class ProjectExtend(models.Model):
    _inherit = "project.project"

    team_id = fields.Many2one("project.team", "Team")
    member_ids = fields.Many2many(
        "project.team.member",
        "Members",
        compute="_compute_member_ids",
        store=False
    )

    @api.depends("team_id", "team_id.team_member_ids")
    def _compute_member_ids(self):
        for rec in self:
            if rec.team_id:
                rec.member_ids = rec.team_id.team_member_ids
            else:
                rec.member_ids = []


class ProjectTaskExtend(models.Model):
    _inherit = "project.task"

    hide_date_assign = fields.Integer(compute="_compute_date_assign_hide", default=0)

    @api.depends("stage_id")
    def _compute_date_assign_hide(self):
        for task in self:
            stage = self.env.ref("project.project_stage_2")
            if task.stage_id == stage:
                task.hide_date_assign = 1
            else:
                task.hide_date_assign = 0

    @api.model
    def create(self, vals):
        if vals.get("date_assign") is None:
            vals["date_assign"] = fields.Datetime.now()
        return super(ProjectTaskExtend, self).create(vals)

    def write(self, vals):
        # Only validate if date_assign is explicitly being updated
        if "date_assign" in vals and vals["date_assign"]:
            if vals["date_assign"] < fields.Datetime.now():
                raise ValidationError("Invalid date assigned.")
        return super(ProjectTaskExtend, self).write(vals)

    def unlink(self):
        for rec in self:
            stage = self.env.ref("project.project_stage_1")
            if rec.stage_id == stage:
                raise UserError("Can not delete IN PROGRESS task.")
        return super(ProjectTaskExtend, self).unlink()

    def action_set_high_priority_task(self):
        for task in self:
            task.priority = "1"


