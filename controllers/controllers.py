from odoo import http

class Managerpurchase(http.Controller):
    @http.route('/create' , auth='public' , type='http' , methods=['GET','POST'])
    def index(self, **kw):
        contact_list={
            'name' : "PR00006"
        }
        return contact_list
