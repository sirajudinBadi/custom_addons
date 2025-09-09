from odoo import http
from odoo.http import request

class CustomerController(http.Controller):

    @http.route("/customers", type="json", auth="user")
    def get_customers(self):
        # You can keep auth="public" if you really want it accessible without login
        customers = request.env["res.partner"].sudo().search_read(
            [("customer_rank", ">", 0)],
            ["name", "email", "phone"]
        )
        return customers or []
