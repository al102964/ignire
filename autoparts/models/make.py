from odoo import models, fields, api

class make(models.Model):
    _name = 'autoparts.make'
    _description = 'autoparts.Make'

    name = fields.Char(string="Make")
    #models = fields.one2Many('autoparts.model',string="Model")