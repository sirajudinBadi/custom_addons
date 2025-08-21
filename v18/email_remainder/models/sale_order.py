# -*-coding:utf-8-*-

from odoo import models,fields,api

class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.model
    def message_post(self, **kwargs):
        partner_ids = kwargs.get("partner_ids", [])
        if partner_ids:
            allowed_partners = self.env["res.partner"].browse(partner_ids).filtered(
                lambda p: not p.restrict_email
            )
            kwargs["partner_ids"] = allowed_partners.ids

        if self:
            restricted_followers = self.message_follower_ids.mapped("partner_id").filtered(
                lambda p: p.restrict_email
            )
            if restricted_followers:
                allowed_followers = self.message_follower_ids.filtered(
                    lambda f: not f.partner_id.restrict_email
                )
                self.message_follower_ids = allowed_followers

        return super(SaleOrder, self).message_post(**kwargs)

