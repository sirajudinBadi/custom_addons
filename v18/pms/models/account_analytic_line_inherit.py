# -*-coding:utf-8-*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class AccountAnalyticLine(models.Model):
    _inherit = "account.analytic.line"

    @api.model
    def create(self, vals):
        record = super().create(vals)

        # only process if timesheet is linked to a task & employee
        if record.task_id and record.employee_id:
            # find the team member linked to this employee's user
            team_member = self.env["project.team.member"].search([
                ("user_id", "=", record.employee_id.user_id.id),
            ], limit=1)

            if not team_member:
                raise ValidationError(
                    f"No project team member found for employee {record.employee_id.name}"
                )

            # write member_id AFTER record is created
            record.member_id = team_member.id

        return record
