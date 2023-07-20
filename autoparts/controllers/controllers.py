# -*- coding: utf-8 -*-
# from odoo import http


# class Auto-parts-categories(http.Controller):
#     @http.route('/auto-parts-categories/auto-parts-categories', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/auto-parts-categories/auto-parts-categories/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('auto-parts-categories.listing', {
#             'root': '/auto-parts-categories/auto-parts-categories',
#             'objects': http.request.env['auto-parts-categories.auto-parts-categories'].search([]),
#         })

#     @http.route('/auto-parts-categories/auto-parts-categories/objects/<model("auto-parts-categories.auto-parts-categories"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('auto-parts-categories.object', {
#             'object': obj
#         })
