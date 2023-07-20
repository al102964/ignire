# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class auto-parts-categories(models.Model):
#     _name = 'auto-parts-categories.auto-parts-categories'
#     _description = 'auto-parts-categories.auto-parts-categories'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
