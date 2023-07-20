from odoo import models, fields, api

class category_2(models.Model):
    _name = 'autoparts.category_2'
    _description = 'autoparts.category_2'

    name = fields.Char(string="Category_2")
    category_1_id = fields.Many2many('autoparts.category_1',string="Category_1")