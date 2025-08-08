# -*-coding:utf-8-*-
from datetime import timedelta

from library.models.library_reservation import LibraryReservation
from odoo import fields, models, api

BORROW_STATUS = [
    ("borrowed", "Borrowed"),
    ("returned", "Returned")
]

class BookBorrow(models.Model):
    _name="library.borrow"
    _inherit = "soft.delete.mixin"

    member_id = fields.Many2one("library.member", "Borrower", required=True)
    book_id = fields.Many2one("library.book", "Book", required=True)
    borrow_date = fields.Date(string="Borrow Date", default=fields.Date.today, readonly=True)
    return_date = fields.Date(string="Return Date")
    due_date = fields.Date(string="Due Date", compute="_compute_due_date", store=True)
    status = fields.Selection(selection = BORROW_STATUS, string="Borrow Status")

    @api.depends("borrow_date")
    def _compute_due_date(self):
        for rec in self:
            rec.due_date = rec.borrow_date + timedelta(days=15)

    def write(self, vals):
        res = super(BookBorrow, self).write(vals)
        daily_rate = 10.0
        for rec in self:
            if rec.return_date and rec.due_date:
                if rec.return_date > rec.due_date:
                    days_late = (rec.return_date - rec.due_date).days  # get days as int
                    fine_amount = days_late * daily_rate

                    existing_fine = self.env["library.fine"].search([("borrow_id", "=", rec.id)], limit=1)
                    if existing_fine:
                        # Update the existing fine amount and status
                        existing_fine.write({
                            "fine_amount": fine_amount,
                            "status": "unpaid"  # or whatever your default status is
                        })
                    else:
                        # Create a new fine record
                        self.env["library.fine"].create({
                            "borrow_id": rec.id,
                            "member_id": rec.member_id.id,
                            "fine_amount": fine_amount,
                            "status": "unpaid"
                        })
                else:
                    # If returned on time or early, clear fine if exists
                    existing_fine = self.env["library.fine"].search([("borrow_id", "=", rec.id)], limit=1)
                    if existing_fine:
                        existing_fine.write({
                            "fine_amount": 0.0,
                            "status": "paid"
                        })
        return res

    @api.model_create_multi
    def create(self, vals_list):
        reservation_model = self.env["library.book.reservation"]
        borrow_vals_list = []

        for vals in vals_list:
            book = self.env["library.book"].browse(vals["book_id"])
            if book.available_copies > 0:
                # Collect borrow vals, not created records
                borrow_vals_list.append(vals)
            else:
                # Create reservation with a list of dicts (even if one)
                reservation_model.create([{
                    "member_id": vals["member_id"],
                    "book_id": vals["book_id"]
                }])

        # Create all borrow records at once
        if borrow_vals_list:
            return super(BookBorrow, self).create(borrow_vals_list)
        else:
            return self.env["library.borrow"]  # empty recordset
