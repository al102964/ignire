from odoo import models, fields, api

class category_1(models.Model):
    _name = 'autoparts.category_1'
    _description = 'autoparts.category_1'

    name = fields.Char(string="Category_1")
    #models = fields.one2Many('autoparts.model',string="Model")