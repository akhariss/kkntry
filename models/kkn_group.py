# -*- coding: utf-8 -*-
from odoo import models, fields, api

class KknGroup(models.Model):
    _name = 'tipd_kkn.group'
    _description = 'Kelompok KKN'
    _inherit = ['mail.thread']

    name = fields.Char(string='Nama Kelompok', required=True, tracking=True, help="Contoh: Kelompok 1 - Parepare")
    program_id = fields.Many2one('tipd_kkn.program', string='Program KKN', required=True, tracking=True)
    location_id = fields.Many2one('tipd_kkn.location', string='Posko / Lokasi', tracking=True)
    supervisor_id = fields.Many2one('tipd_kkn.supervisor', string='Dosen Pembimbing (DPL)', tracking=True)
    
    participant_ids = fields.One2many('tipd_kkn.participant', 'group_id', string='Anggota Kelompok')
    activity_ids = fields.One2many('tipd_kkn.activity', 'group_id', string='Laporan Kegiatan')
    
    participant_count = fields.Integer(string='Jumlah Anggota', compute='_compute_participant_count')

    @api.depends('participant_ids')
    def _compute_participant_count(self):
        for record in self:
            record.participant_count = len(record.participant_ids)
