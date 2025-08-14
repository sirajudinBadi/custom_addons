# -*-coding:utf-8-*-

from odoo import models, fields, api


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
