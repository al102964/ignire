from odoo import models, fields, api

class category_3(models.Model):
    _name = 'autoparts.category_3'
    _description = 'autoparts.category_3'

    name = fields.Char(string="Category_3")
    category_2_id = fields.Many2many('autoparts.category_2',string="Category_2")
    category_1 = fields.Many2many(related="category_2_id.category_1_id", readonly=False, string="Category_1")