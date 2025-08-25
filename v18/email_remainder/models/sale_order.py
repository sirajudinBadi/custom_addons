# -*-coding:utf-8-*-

from odoo import models, api
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.model
    def _notify_get_recipients(self, message, msg_vals, **kwargs):
        recipients = super()._notify_get_recipients(message, msg_vals, **kwargs)

        partners = []
        for r in recipients:
            partner = self.env['res.partner'].browse(r['id'])
            if partner.restrict_email:
                continue
            else:
                partners.append(r)

        recipients = partners

        return recipients
