# -*- coding: utf-8 -*-
##############################################################################
#
# Part of Caret IT Solutions Pvt. Ltd. (Website: www.caretit.com).
# See LICENSE file for full copyright and licensing details.
#
##############################################################################

from odoo import http
from odoo.exceptions import ValidationError
from odoo.http import request
# from odoo.addons.portal.controllers.portal import CustomerPortal

class PortalLeaveController(http.Controller):

    @http.route(['/my/leaves'], type='http', auth="user", website=True)
    def get_leaves(self):
        leaves = request.env["hr.leave"].sudo().search([
            ('employee_id.user_id', '=', request.env.user.id)
        ])
        print(f"Leaves: {leaves}")
        return request.render("portal_leave.leave_list_template", {"leaves":leaves})

    @http.route("/my/leaves/apply", type="http", auth="user", website=True)
    def apply_leave(self, **kwargs):
        leave_types = request.env['hr.leave.type'].sudo().search([])
        selected_leave_type = leave_types.filtered(
            lambda l: l.id == int(kwargs.get('holiday_status_id', 0))) if kwargs.get('holiday_status_id') else None
        return request.render("portal_leave.leave_application_template", {"leave_types":leave_types, "selected_leave_type":selected_leave_type,})

    @http.route("/my/leaves/submit", type="http", auth="user", website=True, methods=['POST'])
    def request_leave(self, **data):
        employee = request.env['hr.employee'].sudo().search([('user_id', '=', request.env.user.id)], limit=1)
        if employee:
            request.env["hr.leave"].sudo().create({
                'name': data.get('description'),
                'holiday_status_id': int(data.get('holiday_status_id')),
                'request_date_from': data.get('request_date_from'),
                'request_date_to': data.get('request_date_to'),
                'employee_id': employee.id,
            })
            return request.redirect("my/leaves")
        return ValidationError("Unauthorized")