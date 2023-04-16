# -*- coding: utf-8 -*-
#################################################################################
#
# Copyright (c) 2018-Present Webkul Software Pvt. Ltd. (<https://webkul.com/>:wink:
# See LICENSE file for full copyright and licensing details.
#################################################################################
from odoo import api, fields, models, _

class ResPartner(models.Model):
	_inherit = 'res.groups'
	
	# nama_group = 
	# wk_dob = fields.Date( string='Date of Birth')
	jeneng = fields.Char(required=True, translate=True)
	kategori = fields.Many2one('ir.module.category', string='Applicationxyyyy', index=True)
# fields.Many2one('ir.module.category', string='Applicationxxxxx', index=True)