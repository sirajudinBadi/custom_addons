# -*-coding:utf-8-*-
from odoo import models,fields,api

class ReportProjectTimesheet(models.AbstractModel):
    _name = "report.report_generator.project_timesheet_report"
    _description = "Project Task Timesheet Report"

    @api.model
    def _get_report_values(self,docids, data=None):
        date_from = data.get("date_from")
        date_to = data.get("date_to")

        domain = [
            ("date", '>=', date_from),
            ('date', '<=', date_to),
        ]
        company = self.env.company
        timesheets = self.env["account.analytic.line"].sudo().search(domain,order="project_id, task_id, date")
        grouped_data = {}

        for ts in timesheets:
            project = ts.project_id
            task = ts.task_id

            # ensure project key exists
            if project not in grouped_data:
                grouped_data[project] = {}

            # ensure task key exists under project
            if task not in grouped_data[project]:
                grouped_data[project][task] = []

            # add timesheet to that task group
            grouped_data[project][task].append(ts)
        return {
            "doc_ids" : timesheets.ids,
            "doc_model" : "account.analytic.line",
            "data" : data,
            "company" : company,
            "grouped_data" : grouped_data,
            "date_from" : date_from,
            "date_to" : date_to,
        }