# -*- coding: utf-8 -*-
from odoo import models, fields, api

class KknProgram(models.Model):
    _name = 'tipd_kkn.program'
    _description = 'Program KKN'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Nama Program', required=True, tracking=True, help="Contoh: KKN Reguler Angkatan 10")
    year = fields.Char(string='Tahun', required=True, tracking=True)
    theme = fields.Char(string='Tema KKN')
    start_date = fields.Date(string='Tanggal Mulai', required=True, tracking=True)
    end_date = fields.Date(string='Tanggal Selesai', required=True, tracking=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('active', 'Aktif'),
        ('done', 'Selesai'),
        ('cancel', 'Dibatalkan'),
    ], string='Status', default='draft', tracking=True)
    active = fields.Boolean(default=True)
    
    group_ids = fields.One2many('tipd_kkn.group', 'program_id', string='Daftar Kelompok')
    participant_count = fields.Integer(string='Jumlah Peserta', compute='_compute_participant_count')

    @api.depends('group_ids.participant_ids')
    def _compute_participant_count(self):
        for record in self:
            count = 0
            for group in record.group_ids:
                count += len(group.participant_ids)
            record.participant_count = count
