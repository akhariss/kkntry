# -*- coding: utf-8 -*-
from odoo import models, fields

class KknSupervisor(models.Model):
    _name = 'tipd_kkn.supervisor'
    _description = 'Dosen Pembimbing Lapangan'
    _rec_name = 'partner_id'

    partner_id = fields.Many2one('res.partner', string='Dosen (DPL)', required=True, domain=[('is_company', '=', False)])
    nip = fields.Char(string='NIP / NIDN', related='partner_id.ref', readonly=False, store=True)
    
    group_ids = fields.One2many('tipd_kkn.group', 'supervisor_id', string='Kelompok Bimbingan')
    program_id = fields.Many2one('tipd_kkn.program', string='Program KKN')
