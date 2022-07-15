from odoo import  api , fields , models

class Lostreason(models.TransientModel):
    _name = "lost.reason"
    _description = "Get lost reason"

    reason = fields.Char(string="Lost reason" , required = True)
