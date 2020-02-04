# -*- coding: utf8 -*-
from odoo import models, fields

class OpenAcademyCours(models.Model):
    _name = 'openacademy.course'
    _description = 'OpenAcademy Course'
    
    name = fields.char(string='Course Tilte', required=True,
                      index=True, help='Enter your course title on this field,')
    description = fields.html(string'Description')
    banner = fields.Binary(string='Banner')
    price = fields.float(string='Price' Digits (5,4))
    expire_date = fields.date(string='Expire After', required=True)
    
