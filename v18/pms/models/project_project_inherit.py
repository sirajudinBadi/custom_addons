# -*-coding:utf-8-*-

from odoo import models, fields, api
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
    description_text = fields.Text(string="Description", index=True, help="Indexing speeds up data retrieval but slower data storage.")

    @api.depends("team_id", "team_id.team_member_ids")
    def _compute_member_ids(self):
        for rec in self:
            if rec.team_id:
                rec.member_ids = rec.team_id.team_member_ids
            else:
                rec.member_ids = []


class ProjectTaskExtend(models.Model):
    _inherit = "project.task"

    date_assign = fields.Datetime("Assigned Date", help="Date of assignment")

    hide_date_assign = fields.Boolean(compute="_compute_date_assign_hide", store=False)

    @api.depends("stage_id")
    def _compute_date_assign_hide(self):
        for task in self:
            stage = self.env.ref("project.project_stage_2")
            if task.stage_id == stage:
                task.hide_date_assign = True
            else:
                task.hide_date_assign = False

    @api.constrains('date_assign')
    def check_assigned_date(self):
        for rec in self:
            if rec.date_assign and rec.date_assign < fields.Datetime.now():
                raise ValidationError("Assigned Date can not be earlier then current time.")

    @api.model
    def create(self, vals):
        if vals.get("date_assign") is None:
            vals["date_assign"] = fields.Datetime.now()
        return super(ProjectTaskExtend, self).create(vals)

    # def write(self, vals):
    #     # Only validate if date_assign is explicitly being updated
    #     if "date_assign" in vals and vals["date_assign"]:
    #         if vals["date_assign"] < fields.Datetime.now():
    #             raise ValidationError("Invalid date assigned.")
    #     return super(ProjectTaskExtend, self).write(vals)

    def unlink(self):
        for rec in self:
            stage = self.env.ref("project.project_stage_1")
            if rec.stage_id == stage:
                raise UserError("Can not delete tasks that are in progress.")
        return super(ProjectTaskExtend, self).unlink()

    def action_set_high_priority_task(self):
        for task in self:
            task.priority = "1"

