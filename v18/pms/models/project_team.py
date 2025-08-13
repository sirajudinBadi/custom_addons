# -*-coding:utf-8-*-

from odoo import models, fields, api


class ProjectTeam(models.Model):
    _name = "project.team"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = "name asc"
    _description = "Teams"

    name = fields.Char(string="Team Name", tracking=True, required=True)
    team_leader = fields.Char(string="Team Leader", required=True, tracking=True)
    team_member_ids = fields.Many2many(
        "project.team.member",
        "team_and_member_rel",
        "team_id",
        "member_id",
        string="Team Members"
    )
    active = fields.Boolean(string="Status", default=True)
    sequence = fields.Char(string="Sequence", readonly=True, copy=False, default="New")

    @api.model
    def create(self, vals):
        if vals.get("sequence", "New") == "New":
            seq_prefix = self.env["ir.sequence"].next_by_code("project.sequence") or "New"
            vals["sequence"] = f"{seq_prefix}/{vals.get('name')}/{fields.Date.today()}"
        return super(ProjectTeam, self).create(vals)
