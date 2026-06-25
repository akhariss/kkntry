# -*- coding: utf-8 -*-
from odoo import models, fields

class KknParticipant(models.Model):
    _name = 'tipd_kkn.participant'
    _description = 'Peserta KKN'
    _inherit = ['mail.thread']
    _rec_name = 'partner_id'

    partner_id = fields.Many2one('res.partner', string='Mahasiswa', required=True, tracking=True, domain=[('is_company', '=', False)])
    nim = fields.Char(string='NIM / Stambuk', related='partner_id.ref', readonly=False, store=True)
    
    group_id = fields.Many2one('tipd_kkn.group', string='Kelompok KKN', tracking=True)
    program_id = fields.Many2one('tipd_kkn.program', string='Program KKN', tracking=True)
    
    faculty = fields.Char(string='Fakultas')
    major = fields.Char(string='Program Studi')
    
    status = fields.Selection([
        ('registered', 'Terdaftar'),
        ('active', 'Aktif'),
        ('withdrawn', 'Mengundurkan Diri'),
        ('completed', 'Selesai')
    ], string='Status Peserta', default='registered', tracking=True)
    
    grade_ids = fields.One2many('tipd_kkn.grade', 'participant_id', string='Nilai')
