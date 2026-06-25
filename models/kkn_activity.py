# -*- coding: utf-8 -*-
from odoo import models, fields

class KknActivity(models.Model):
    _name = 'tipd_kkn.activity'
    _description = 'Laporan Kegiatan Harian (LKH)'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Judul Kegiatan', required=True, tracking=True)
    date = fields.Date(string='Tanggal Pelaksanaan', default=fields.Date.context_today, required=True, tracking=True)
    
    group_id = fields.Many2one('tipd_kkn.group', string='Kelompok', required=True, tracking=True)
    participant_id = fields.Many2one('tipd_kkn.participant', string='Dilaporkan Oleh', tracking=True)
    
    description = fields.Html(string='Uraian Kegiatan', required=True)
    
    state = fields.Selection([
        ('draft', 'Draft'),
        ('submitted', 'Diajukan'),
        ('approved', 'Disetujui DPL'),
        ('rejected', 'Ditolak')
    ], string='Status', default='draft', tracking=True)
