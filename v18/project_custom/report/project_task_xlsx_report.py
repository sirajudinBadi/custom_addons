# -*-coding:utf-8-*-

from odoo import models

class ProjectTaskReportXlsx(models.AbstractModel):
    _name = 'report.project_custom.project_task_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self,workbook,data,tasks):
        sheet = workbook.add_worksheet('Tasks')
        bold = workbook.add_format({"bold":True})

        headers = ['Task Name', 'Start Date', "End Date"]
        for col,header in enumerate(headers):
            sheet.write(0,col,header,bold)

        for row,task in enumerate(tasks,start=1):
            sheet.write(row,0,task.name)
            sheet.write(row,1,str(task.date_start) or '')
            sheet.write(row,2,str(task.date_end) or '')
