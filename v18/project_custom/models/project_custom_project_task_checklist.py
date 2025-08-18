# -*-coding:utf-8-*-

from odoo import models,fields,api

class ProjectTaskChecklist(models.Model):
    """
    This model inherits the project.task and startend.mixin(Abstract Model). (Extension Inheritance)
    This model also uses the Delegation Inheritance using 'project.task' model.
    """

    _name = "project.task.checklist"

    _inherit = ["startend.mixin", "project.task"]
    _inherits = {
        "project.task" : "task_id",
    }