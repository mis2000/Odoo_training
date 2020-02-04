# -*- coding: utf8 -*-
from odoo import models, fields

class OpenAcademyCours(models.Model):
    _name = 'openacademy.course'
    _description = 'OpenAcademy Course'

    
class OpenAcademyTags(models.Model):
    _name = 'openacademy.tags'
    _description = 'Openacademy Tags'
    name = fields.char(string='Name')
    
    
    
    name = fields.char(string='Course Tilte', required=True,
                      index=True, help='Enter your course title on this field,')
    description = fields.html(string'Description')
    banner = fields.Binary(string='Banner')
    price = fields.float(string='Price' Digits (5,4))
    expire_date = fields.date(string='Expire After', required=True)
    
    responsible_id = fields.Many2one(comodel_name='res.users', required=True, string='Responsible',
                                   ondelete='restrict', copy='False')
    
    tag_ids = fields.Many2Many(comodel_name='openacademy.tags', relation='rel_course_tags',
                              column1='course_id', column2='Tag_Id', string='Tags')