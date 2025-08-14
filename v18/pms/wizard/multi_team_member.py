# -*-coding:utf-8-*-

from odoo import models,fields,api
from odoo.exceptions import ValidationError


class MultiTeamMemberAdd(models.TransientModel):
    _name = "multi.team.member"
    _description = "Add member to multiple team"

    member_id = fields.Many2one("project.team.member", string="Member")

    def action_add_member_to_multi_teams(self):
        active_ids = self.env.context.get("active_ids", [])
        if not active_ids:
            raise ValidationError("Select Teams")

        teams = self.env["project.team"].browse(active_ids)
        for team in teams:
            team.team_member_ids = [(4, self.member_id.id)]
        return {
            "type" : "ir.actions.act_window_close"
        }
