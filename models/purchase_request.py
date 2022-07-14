from odoo import  api , fields , models

class Purchaserequest(models.Model):
    _name = "purchase.request"
    _description = "Purchase request"

    department_id = fields.Many2one("hr.department", string="Department" , required=True)
    request_id = fields.Many2one("res.users" , required=True)
    approver_id = fields.Many2one("res.users", string="approver" , required=True)
    date = fields.Date(string="Date", default=fields.Date.today() , readonly=True )
    date_approve = fields.Date(string="Date approve" , required=True)
    request_line_ids =fields.One2many("purchase.request.line" , "request_id" , required=True)
    description = fields.Text(string="Description" )
    state = fields.Selection([("draft", "Draft"), ("wait", "Wait"), ("approved", "Approved"), ("cancel", "Cancel")],
                             default="draft" , required=True)
    total_qty = fields.Integer(string="Total qty")
    total_amount = fields.Float(string="Total amount")

    @api.returns('mail.message', lambda value: value)
    def request_user(self):
        self.write({'state': 'wait'})
        return {}

