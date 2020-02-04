# -*- coding: utf-8 -*-
# from odoo import http


# class Openacadimy(http.Controller):
#     @http.route('/openacadimy/openacadimy/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/openacadimy/openacadimy/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('openacadimy.listing', {
#             'root': '/openacadimy/openacadimy',
#             'objects': http.request.env['openacadimy.openacadimy'].search([]),
#         })

#     @http.route('/openacadimy/openacadimy/objects/<model("openacadimy.openacadimy"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('openacadimy.object', {
#             'object': obj
#         })
