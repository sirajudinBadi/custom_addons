from odoo import http
from odoo.http import request


class CrmController(http.Controller):

    @http.route("/leads", type="http", auth="public", website=True)
    def list_partners(self):
        leads = request.env["crm.lead"].sudo().search([])
        return request.render("custom_web.crm_lead_list_template", {"leads" : leads})

    @http.route("/leads/form", type='http', auth='public',website=True)
    def partner_form(self):
        partners = request.env["res.partner"].sudo().search([])
        return request.render("custom_web.crm_lead_form_template",{"partners":partners})

    @http.route("/leads/form/submit", type="http", auth="public", methods=["POST"], website=True, csrf=True)
    def partner_form_submit(self,**data):
        request.env["crm.lead"].sudo().create({
            "name" : data.get("name"),
            "partner_id" : int(data.get("partner_id")) if data.get("partner_id") else False,
            "email_from" : data.get("email_from"),
            "expected_revenue" : data.get("expected_revenue"),
            "probability" : data.get("probability"),
        })
        return request.redirect("/leads")

    @http.route("/leads/<int:lead_id>/edit", type="http", auth="public", website=True)
    def edit_lead_form(self, lead_id):
        lead = request.env["crm.lead"].sudo().browse(lead_id)
        if not lead.exists():
            return request.not_found()
        return request.render("custom_web.crm_lead_edit_template", {"lead" : lead})

    @http.route("/leads/<int:lead_id>/update", type="http", auth="public", methods=["POST"], website=True, csrf=False)
    def update_lead(self, lead_id, **data):
        lead = request.env["crm.lead"].sudo().browse(lead_id)
        if not lead.exists():
            return request.not_found()

        values = {
            "name": data.get("name"),
            "email_from": data.get("email_from"),
            "expected_revenue": data.get("expected_revenue"),
            "probability": data.get("probability"),
        }

        # Only write partner_id if provided
        partner_id = data.get("partner_id")
        if partner_id and partner_id.isdigit():
            values["partner_id"] = int(partner_id)

        lead.write(values)

        return request.redirect("/leads")