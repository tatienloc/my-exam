from odoo import  api , fields , models

class Purchaserequest(models.Model):
    _name = "purchase.request"
    _description = "Purchase request"

    department_id = fields.Many2one("hr.department", string="Department" , required=True)
    request_id = fields.Many2one("res.users")
    approver_id = fields.Many2one("res.users", string="approver")
    date = fields.Date(string="Date", default=fields.Date.today() , readonly=True)
    date_approve = fields.Date(string="Date approve")
    request_line_ids =fields.One2many("purchase.request.line" , "request_id")
    description = fields.Text(string="Description")
    state = fields.Selection([("Draft", "draft"), ("Wait", "wait"), ("Approved", "approved"), ("Cancel", "cancel")],
                             default="Draft")
    total_qty = fields.Integer(string="Total qty")
    total_amount = fields.Float(string="Total amount")

