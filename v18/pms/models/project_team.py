# -*-coding:utf-8-*-

from odoo import models,fields,api

class ProjectTeam(models.Model):
    _name = "project.team"
    _order = "name asc"
    _description = "Teams"

    name = fields.Char(string="Team Name", required=True)
    team_leader = fields.Char(string="Team Leader", required=True)
    team_member_ids = fields.Many2many(
        "project.team.member",
        "team_and_member_rel",
        "team_id",
        "member_id",
        string="Team Members"
    )
    active = fields.Boolean(string="Status", default=True)
