# -*- coding: utf-8 -*-

from odoo import fields, models, api
from datetime import datetime

class SoftDeleteMixin(models.AbstractModel):
    _name = "soft.delete.mixin"
    _description = "Soft Delete Mixin"

    is_deleted = fields.Boolean(default=False, index=True)
    deleted_at = fields.Datetime(string="Deleted At", readonly=True)

    def unlink(self):
        for record in self:
            record.write({
                'is_deleted' : True,
                "deleted_at" : fields.Datetime.now(),
                "active" : False
            })
        return True

    # @api.model
    # def search(self, domain, offset=0, limit=None, order=None, count=False):
    #     if not any(d[0] == 'is_deleted' for d in domain):
    #         domain += [('is_deleted', '=', False)]
    #     return super(SoftDeleteMixin, self).search(domain, offset=offset, limit=limit, order=order, count=count)

    @api.model
    def search(self, domain, offset=0, limit=None, order=None, count=False):
        domain = domain or []
        ctx = self._context or {}

        # DEBUG: print to logs
        print("SEARCH CONTEXT:", ctx)
        print("SEARCH DOMAIN (before):", domain)

        # Only modify if not explicitly including deleted records
        if not any(d[0] == 'is_deleted' for d in domain) and not ctx.get('include_deleted'):
            domain += [('is_deleted', '=', False)]

        print("SEARCH DOMAIN (after):", domain)

        return super().search(domain, offset=offset, limit=limit, order=order)

    def hard_unlink(self):
        return super().unlink()

    def restore(self):
        for record in self:
            if record.is_deleted:
                record.write({
                    'is_deleted': False,
                    'deleted_at': None,
                    'active': True,
                })
        return True