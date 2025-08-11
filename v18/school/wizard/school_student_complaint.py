# -*-coding:utf-8-*-

from odoo import models, fields, api, _

class SchoolStudentComplaint(models.TransientModel):
    _name = "school.student.complaint"
    _description = "Student Complaints"

    student_id = fields.Many2one("school.student", string="Student", required=True)
    complaint = fields.Text(string="Complaint Text", required=True)

