# -*- coding: utf-8 -*-
# from odoo import http


# class Managerpurchase(http.Controller):
#     @http.route('/managerpurchase/managerpurchase/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/managerpurchase/managerpurchase/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('managerpurchase.listing', {
#             'root': '/managerpurchase/managerpurchase',
#             'objects': http.request.env['managerpurchase.managerpurchase'].search([]),
#         })

#     @http.route('/managerpurchase/managerpurchase/objects/<model("managerpurchase.managerpurchase"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('managerpurchase.object', {
#             'object': obj
#         })
