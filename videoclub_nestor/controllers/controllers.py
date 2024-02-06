# -*- coding: utf-8 -*-
# from odoo import http


# class VideoclubNestor(http.Controller):
#     @http.route('/videoclub_nestor/videoclub_nestor', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/videoclub_nestor/videoclub_nestor/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('videoclub_nestor.listing', {
#             'root': '/videoclub_nestor/videoclub_nestor',
#             'objects': http.request.env['videoclub_nestor.videoclub_nestor'].search([]),
#         })

#     @http.route('/videoclub_nestor/videoclub_nestor/objects/<model("videoclub_nestor.videoclub_nestor"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('videoclub_nestor.object', {
#             'object': obj
#         })

