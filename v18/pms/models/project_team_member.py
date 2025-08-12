# -*-coding:utf-8-*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError

MEMBER_GENDER_SELECTION = [
    ("female", "Female"),
    ("male", "Male"),
    ("other", "Other")
]

class ExtendedAnalyticLine(models.Model):
    _inherit = "account.analytic.line"

    member_id = fields.Many2one("project.team.member", string="Member", required=True)


class ExtendedUsers(models.Model):
    _inherit = "res.users"
    _rec_name = "display_name"

    employee_id = fields.One2many("hr.employee", "user_id")
    # employee_detail_id = fields.Many2one("hr.employee")
    #
    # emp_name = fields.Char(related="employee_detail_id.name")
    # emp_email= fields.Char(related="employee_detail_id.work_email")
    #
    # display_name = fields.Char(string="Display Detail", compute="_compute_display_name", store=True)

    @api.depends("name", "login")
    def _compute_display_name(self):
        for rec in self:
            if rec.name and rec.login:
                rec.display_name = f"{rec.name} / {rec.login}"

class ProjectTeamMember(models.Model):
    _name = "project.team.member"
    _description = "Project Team Member"
    _rec_name = "name"
    _order = "name"
    _copy = False

    name = fields.Char(string="Name", required=True, help="Team member name")

    house_no = fields.Char(string="House No.")
    street = fields.Char(string="Street")
    street2 = fields.Char(string="Street-2")
    country_id = fields.Many2one("res.country", string="Country", required=True)
    state_id = fields.Many2one("res.country.state", string="State", required=True)
    city_id = fields.Many2one("res.state.city", string="City", required=True)
    zipcode = fields.Char(string="Zip Code", help="Zip/Postal code of 6 letters", required=True)

    mobile = fields.Char(string="Mobile No.", required=True)
    user_id = fields.Many2one("res.users", string="User", required=True, context={"search_default_employee" : 1}, domain="[('employee_type', '=', 'employee')]")
    email = fields.Char(related="user_id.email", string="Email")

    gender = fields.Selection(selection=MEMBER_GENDER_SELECTION, required=True)
    birth_date = fields.Date(string="Birth Date", required=True)

    user_image = fields.Binary(string="User Image", attachment=True)
    bio_data = fields.Html(string="Bio-Data", required=True)

    active = fields.Boolean(string="Active Status", default=True)
    timesheet_ids = fields.One2many("account.analytic.line","member_id", string="Timesheet")

    _sql_constraints = [
        ("unique_mobile", "unique(mobile)", "Mobile number must be unique."),
    ]

    @api.constrains("zipcode")
    def validate_fields(self):
        for rec in self:
            if rec.zipcode and rec.mobile and rec.birth_date:
                zipcode = rec.zipcode.strip()
                mobile = rec.mobile.strip()
                if not len(zipcode) == 6:
                    raise ValidationError("Zipcode must be of 6 digits.")
                if not len(mobile) == 10:
                    raise ValidationError("Mobile no. must be of 10 digits")

                if rec.birth_date >= fields.Date.today():
                    raise ValidationError("Invalid Birth Date.")

    def copy(self):
        raise ValidationError("Can not Duplicate record.")

