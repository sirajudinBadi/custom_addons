# -*-coding:utf-8-*-

from odoo import models, api
from odoo.exceptions import ValidationError
import re

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.model
    def _notify_get_recipients(self, message, msg_vals, **kwargs):
        recipients = super()._notify_get_recipients(message, msg_vals, **kwargs)

        # get subtype safely
        subtype_id = msg_vals.get("subtype_id") if msg_vals else message.subtype_id.id
        body = msg_vals.get("body") if msg_vals else (message.body or "")

        # extract mentioned partners
        mentioned_partner_ids = set(map(int, re.findall(r'id=(\d+)&model=res\.partner', body)))

        allowed_recipients = []

        for r in recipients:
            partner = self.env['res.partner'].browse(r['id'])

            if subtype_id == 1:  # Send Message
                if not partner.restrict_email:
                    allowed_recipients.append(r)
                # restricted → skipped
                continue

            elif subtype_id == 2:  # Log Note
                print("Log NOTE")
                if partner.restrict_email:
                    print("Inside lognote Restricted partner")

                    # allow mail but prevent auto-follow
                    r['is_follower'] = False
                    print(f"Reached")
                    allowed_recipients.append(r)
                    # else restricted & not mentioned → skip
                else:
                    r["is_follower"] = True
                    allowed_recipients.append(r)
                continue

            else:
                # fallback (other subtypes)
                allowed_recipients.append(r)

        return allowed_recipients
