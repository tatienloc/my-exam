from odoo import  api , fields , models

class Purchaserequest(models.Model):
    _name = "purchase.request"
    _description = "Purchase request"

    name = fields.Char( required=True, index=True, copy=False,
                       default='New')
    department_id = fields.Many2one("hr.department", string="Department" , required=True)
    request_id = fields.Many2one("res.users" , required=True)
    approver_id = fields.Many2one("res.users", string="Approver" , required=True)
    date = fields.Date(string="Date", default=fields.Date.today() , readonly=True )
    date_approve = fields.Date(string="Date approve" , required=True)
    request_line_ids =fields.Many2many("purchase.request.line" , string="Request line" )
    description = fields.Text(string="Description" )
    state = fields.Selection([("draft", "Draft"), ("wait", "Wait"), ("approved", "Approved"), ("cancel", "Cancel")],
                             default="draft" , required=True)
    total_qty = fields.Float(string="Total qty" , readonly=True )
    total_amount = fields.Float(string="Total amount")


    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('purchase.request') or 'New'
        result = super(Purchaserequest, self).create(vals)
        return result

    @api.returns('mail.message', lambda value: value)
    def request_user(self):
        self.write({'state': 'wait'})
        return {}

    def back_draft(self):
        self.write({'state': 'draft'})
        return {}

    def manager_approve(self):
        self.write({'state': 'approved'})
        return {}





