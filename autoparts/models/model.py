from odoo import models, fields, api

class model(models.Model):
    _name = 'autoparts.model'
    _description = 'autoparts.model'

    name = fields.Char(string="Model")
    make_id = fields.Many2one('autoparts.make',string="Make")