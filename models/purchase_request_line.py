from odoo import  api , fields , models

class Purchaserequestline(models.Model):
    _name = "purchase.request.line"
    _description = "Purchase request line"

    request_id = fields.Many2one("purchase.request" , string="Request ")
    product_id = fields.Many2one("product.template" , string="Product ")
    uom_id = fields.Many2one("uom.uom" , string="Unit")
    qty = fields.Float(string="Qty")
    qty_approve = fields.Float(string="Qty approve")
    total = fields.Float(string="Total" , readonly=True , compute="_compute_total")

    @api.depends("qty" , "product_id")
    def _compute_total(self):
        for r in self:
            r.total = r.qty * r.product_id.list_price




