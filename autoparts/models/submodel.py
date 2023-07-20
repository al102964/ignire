from odoo import models, fields, api

class submodel(models.Model):
    _name = 'autoparts.submodel'
    _description = 'autoparts.submodel'

    name = fields.Char(string="SubModel")
    model_id = fields.Many2one('autoparts.model',string="Model")
    make = fields.Many2one(related="model_id.make_id", readonly=False, string="Make")