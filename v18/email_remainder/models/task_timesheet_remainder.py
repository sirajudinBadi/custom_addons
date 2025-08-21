# -*-coding:utf-8-*-
from datetime import timedelta

from odoo import models, fields, api


class TaskTimesheetRemainder(models.Model):
    _name = "task.timesheet.remainder"
    _description = "Task & Timesheet Remainder via Email"

    @api.model
    def send_daily_remainders(self):
        today = fields.Date.today()
        tomorrow = today + timedelta(days=1)

        tasks = self.env['project.task'].search([
            ("date_deadline", ">=", today - timedelta(days=1)),
        ])

        for task in tasks:
            if not task.date_deadline:
                continue

            deadline_date = task.date_deadline.date()

            for user in task.user_ids:
                subject, body = None, None
                if deadline_date == today:
                    subject = f"Task Due Today: {task.name}"
                    body = f"Reminder: Your task '{task.name}' is due today ({deadline_date})."
                elif deadline_date == tomorrow:
                    subject = f"Task Due Tomorrow: {task.name}"
                    body = f"Reminder: Your task '{task.name}' is due tomorrow ({deadline_date})."

                self.env["mail.mail"].sudo().create([{
                    "subject": "Daily Timesheet Summary",
                    "body_html": f"<p>{body}</p>",
                    "email_to": user.email,
                    'auto_delete': True
                }]).send()

    @api.model
    def send_daily_project_timesheet(self):
        today = fields.Date.today()

        timesheets = self.env["account.analytic.line"].search([
            ("date", '=', today),
        ])
        project_summary = {}
        for timesheet in timesheets:
            project = timesheet.project_id
            if project not in project_summary:
                project_summary[project] = []
            project_summary[project].append(timesheet)

        pm_group = self.env.ref("project.group_project_manager")
        project_managers = pm_group.users

        for manager in project_managers:
            manager_projects = [p for p in project_summary.keys() if p.user_id == manager]
            if not manager_projects:
                continue  # skip managers with no projects today
            body_html = f"<h3>Daily Project Timesheet Summary</h3>"
            for project in manager_projects:
                entries = project_summary[project]
                body_html += f"<h4>Project: {project.name}</h4><ul>"
                for entry in entries:
                    body_html += f"<li>{entry.user_id.name} : {entry.name} {entry.unit_amount}</li>"
                body_html += "</ul>"
            print(f"__________________________________\n{body_html} {manager.email}")
            self.env["mail.mail"].sudo().create([{
                "subject": "Daily Timesheet Summary",
                "body_html": body_html,
                "email_to": manager.email,
                'auto_delete': True
            }]).send()
