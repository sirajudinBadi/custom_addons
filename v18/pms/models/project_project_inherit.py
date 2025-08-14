# -*-coding:utf-8-*-

from odoo import models, fields, api


class ProjectExtend(models.Model):
    _inherit = "project.project"

    # team_ids = fields.One2many("project.team", "project_id", string="Teams")
    team_ids = fields.Many2many(
        "project.team",
        "project_team_rel",
        "project_id",
        "team_id",
        string="Teams"
    )