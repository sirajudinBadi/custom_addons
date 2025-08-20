# -*-coding:utf-8-*-

from odoo import models,fields,api

class ProjectTaskChecklist(models.Model):
    """
    Delegation Inheritance is used to sink the fields of another model in current model.
    It does not create new table but defines relation between 2 tables using foreign key.
    The model delegating the fields has its new table created inside database while keeping parent model as it is.
    """
    _name = "project.task.checklist"
    _description = "Project Tasks Checklist"
    _inherit = ["startend.mixin"]
    _inherits = {"project.task" : "task_id"}

    task_id = fields.Many2one("project.task", "Task")