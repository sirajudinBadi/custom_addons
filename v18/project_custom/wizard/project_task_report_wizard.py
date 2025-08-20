# -*-coding:utf-8-*-

from odoo import models
from odoo.exceptions import ValidationError


class ProjectTaskReportWizard(models.TransientModel):
    _name = 'project.task.report.wizard'
    _inherit = 'startend.mixin'

    def _get_tasks(self):
        abc = self.env['project.task'].sudo().search([
            ('date_start', '>=', self.date_start),
            ('date_end', '<=', self.date_end)
        ])
        print("\n\nqqqqqqqqqqqq---", abc)
        return self.env['project.task'].sudo().search([
            ('date_start', '>=', self.date_start),
            ('date_end', '<=', self.date_end)
        ])

    def generate_xlsx(self):
        tasks = self._get_tasks()
        if not tasks:
            raise ValidationError("No any Task found for given date range.")
        return self.env.ref('project_custom.report_task_xlsx').report_action(tasks)

    def generate_pdf(self):
        tasks=self._get_tasks()
        if not tasks:
            raise ValidationError("No any Task found for given date range.")
        return self.env.ref('project_custom.report_task_pdf').report_action(tasks)
