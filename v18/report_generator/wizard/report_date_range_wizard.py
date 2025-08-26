# -*-coding:utf-8-*-

from odoo import models, api, fields
from odoo.exceptions import ValidationError


class DateRangeWizard(models.TransientModel):
    _name = "report.date.range"
    _description = "Date Range Wizard for Report"

    date_from = fields.Date("From", help="Start date for report range.")
    date_to = fields.Date("To", help="End date for report range.")

    @api.constrains("date_from", "date_to")
    def _check_dates(self):
        for rec in self:
            if rec.date_from and rec.date_to and rec.date_from > rec.date_to:
                raise ValidationError("Invalid date range.")

    def print_report(self):
        return self.env.ref("report_generator.action_report_project_timesheet").report_action(
            [],
            data={
                "date_from": self.date_from,
                "date_to": self.date_to,
            }
        )
