# -*-coding:utf-8-*-

from odoo import fields, models, api

REGISTRATION_STATUS = [
    ("reserved", "Reserved"),
    ("fulfilled", "Fulfilled"),
    ("cancelled", "Cancelled")
]

class LibraryReservation(models.Model):
    _name = "library.book.reservation"
    _inherit = "soft.delete.mixin"

    member_id = fields.Many2one("library.member", "Member", required=True)
    book_id = fields.Many2one("library.book", "Book", required=True)
    reservation_date = fields.Date(default=fields.Date.today)
    status = fields.Selection(selection=REGISTRATION_STATUS, default="reserved")