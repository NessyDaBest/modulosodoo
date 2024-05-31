# -*- coding: utf-8 -*-
# from odoo import http


# class ConfiteriaNestor(http.Controller):
#     @http.route('/confiteria_nestor/confiteria_nestor', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/confiteria_nestor/confiteria_nestor/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('confiteria_nestor.listing', {
#             'root': '/confiteria_nestor/confiteria_nestor',
#             'objects': http.request.env['confiteria_nestor.confiteria_nestor'].search([]),
#         })

#     @http.route('/confiteria_nestor/confiteria_nestor/objects/<model("confiteria_nestor.confiteria_nestor"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('confiteria_nestor.object', {
#             'object': obj
#         })

