from odoo import  api , fields , models

class Purchaserequestline(models.Model):
    _name = "purchase.request.line"
    _description = "Purchase request line"

    request_id = fields.Many2one("purchase.request" , string="Request id")
    product_id = fields.Many2one("product.template" , string="Product id")
    uom_id = fields.Many2one("uom.uom")
    qty = fields.Float()
    qty_approve = fields.Float()
    total = fields.Float()
