from odoo import models, fields, api

class part(models.Model):
    _name = 'autoparts.part'
    _description = 'autoparts.part'

    name = fields.Many2one('autoparts.part_name',string="part_name")
    part_number = fields.Char(string="part_number")
    brand_id = fields.Many2one('autoparts.brand',string="brand")
    category_3 = fields.Many2many('autoparts.category_3',string="category_3")
    #category_2 = fields.Many2many(related='category_3.category_2_id', readonly=False, string="category_2")
    #category_1 = fields.Many2many(related='category_2.category_1_id', readonly=False, string="category_1")
    price_regular = fields.Float('price_regular')
    part_attributes = fields.Char("part_attributes")