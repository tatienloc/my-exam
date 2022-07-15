from odoo import  api , fields , models

class Lostreason(models.TransientModel):
    _name = "lost.reason"
    _description = "Get lost reason"

    reason = fields.Char(string="Lost reason" , required = True)

    def action_lost_reason_apply(self):
        active_obj = self.env[self.env.context.get('active_model')].browse(self.env.context.get('active_id'))
        active_obj.write({'state' : 'cancel',})



