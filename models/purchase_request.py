from odoo import  api , fields , models
from odoo.exceptions import ValidationError

class Purchaserequest(models.Model):
    _name = "purchase.request"
    _description = "Purchase request"

    name = fields.Char( required=True, index=True, copy=False,
                       default='New')
    department_id = fields.Many2one("hr.department", string="Department", required=True)
    request_id = fields.Many2one("res.users" , string="Requester" , required=True )
    approver_id = fields.Many2one("res.users", string="Approver" , required=True )
    date = fields.Date(string="Date", default=fields.Date.today() , readonly=True )
    date_approve = fields.Date(string="Date approve" , required=True)
    request_line_ids =fields.Many2many("purchase.request.line" , string="Request line" )
    description = fields.Text(string="Description" )
    state = fields.Selection([("draft", "Draft"), ("wait", "Wait"), ("approved", "Approved"), ("cancel", "Cancel")],
                             default="draft" , required=True)
    total_qty = fields.Float(string="Total qty" , compute="_compute_total_qty" , readonly=True )
    total_amount = fields.Float(string="Total amount" , compute="_compute_total_amount" , readonly=True)

    #tính total qty , total amount
    @api.depends("request_line_ids")
    def _compute_total_amount(self):
        amount = 0
        for r in self.request_line_ids:
            amount += r.total
        self.total_amount = amount

    @api.depends("request_line_ids")
    def _compute_total_qty(self):
        total = 0
        for r in self.request_line_ids:
            total += r.qty
        self.total_qty = total

    # tự nhảy kí tự
    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('purchase.request') or 'New'
        result = super(Purchaserequest, self).create(vals)
        return result

    # button đổi status
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

    #detele ko đúng status , hiện thông báo
    def unlink(self):
        for r in self:
            if r.state == 'draft':
                return super(Purchaserequest,self).unlink()
            else:
                raise ValidationError("You cannot detete %s as it is in %s status" %(self.name ,self.state))

    def write(self, vals):
        for r in self:
            if r.state == 'draft':
                return super(Purchaserequest,self).write(vals)
            else:
                raise ValidationError("You cannot write %s as it is %s status" %(self.name ,self.state))