# -*-coding:utf-8-*-

from odoo import models,fields,api

class ProjectTask(models.Model):
    _name = "project.task"
    _inherit = ["project.task","startend.mixin"]
