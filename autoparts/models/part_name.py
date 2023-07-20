from odoo import models, fields, api

class part_name(models.Model):
    _name = 'autoparts.part_name'
    _description = 'autoparts.part_name'

    name = fields.Char(string="part_name")