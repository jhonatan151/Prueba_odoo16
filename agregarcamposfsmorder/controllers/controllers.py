# -*- coding: utf-8 -*-
# from odoo import http


# class Agregarcamposfsmorder(http.Controller):
#     @http.route('/agregarcamposfsmorder/agregarcamposfsmorder', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/agregarcamposfsmorder/agregarcamposfsmorder/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('agregarcamposfsmorder.listing', {
#             'root': '/agregarcamposfsmorder/agregarcamposfsmorder',
#             'objects': http.request.env['agregarcamposfsmorder.agregarcamposfsmorder'].search([]),
#         })

#     @http.route('/agregarcamposfsmorder/agregarcamposfsmorder/objects/<model("agregarcamposfsmorder.agregarcamposfsmorder"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('agregarcamposfsmorder.object', {
#             'object': obj
#         })
