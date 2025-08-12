# -*- coding:utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class City(models.Model):
    _name = "res.state.city"
    _description = "Indian Cities"
    _order = "name asc"
    _rec_name = "name"

    name = fields.Char(string="City", required=True)
    rto_code = fields.Char(string="RTO Code", help="RTO Code for state within Gujarat", required=True)

    _sql_constraints = [
        ("unique_name", 'unique(name)', "City must be unique."),
        ("unique_rto_code", "unique(rto_code)", "RTO Code must be unique.")
    ]

    @api.constrains("rto_code", "name")
    def validate_fields(self):
        for rec in self:
            if rec.name and rec.rto_code:
                name = rec.name.strip().title()
                rto_code = rec.rto_code.strip().upper()
                if not name.replace(" ", "").isalpha():
                    raise ValidationError("Name should only include alphabet and spaces")
                if not rto_code.startswith("GJ"):
                    raise ValidationError("RTO Code must start with GJ.")