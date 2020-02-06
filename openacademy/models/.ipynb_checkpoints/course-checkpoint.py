# -*- coding: utf8 -*-
from odoo import models, fields

class OpenAcademyTags(models.Model):
    _name = 'openacademy.tags'
    _description = 'Openacademy Tags'
    name = fields.Char(string='Name')


class OpenAcademyCours(models.Model):
    _name = 'openacademy.course'
    _description = 'OpenAcademy Course'   
    
    name = fields.Char(string='Course Tilte', required=True,
                      index=True, help='Enter your course title on this field,')
    description = fields.Html(string='Description')
    active = fields.Boolean(string='Archived', default=False)
    banner = fields.Binary(string='Banner')
    price = fields.Float(string='Price', digits=(5,2))
    expire_date = fields.Date(string='Expire After', required=True)
    
    responsible_id = fields.Many2one(comodel_name='res.users', required=True, 
                        string='Responsible', ondelete='restrict', copy=False)
    
    tag_ids = fields.Many2many(comodel_name='openacademy.tags', relation='rel_course_tags',
                              column1='course_id', column2='Tag_Id', string='Tags')
    