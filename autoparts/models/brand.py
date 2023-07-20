from odoo import models, fields, api

class brand(models.Model):
    _name = 'autoparts.brand'
    _description = 'autoparts.brand'

    name = fields.Char(string="brand")