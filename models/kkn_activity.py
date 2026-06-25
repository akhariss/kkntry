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

    def action_submit(self):
        for record in self:
            record.state = 'submitted'

    def action_approve(self):
        for record in self:
            record.state = 'approved'
            # Cari atau buat blog khusus KKN
            blog = self.env['blog.blog'].search([('name', 'ilike', 'Berita KKN')], limit=1)
            if not blog:
                blog = self.env['blog.blog'].create({
                    'name': 'Berita KKN',
                    'subtitle': 'Publikasi Kegiatan Mahasiswa KKN'
                })
            
            # Buat postingan blog
            author_id = self.env.user.partner_id.id
            if record.participant_id and record.participant_id.partner_id:
                author_id = record.participant_id.partner_id.id
                
            self.env['blog.post'].create({
                'name': record.name,
                'subtitle': f'Dilaporkan oleh {record.participant_id.name} ({record.group_id.name}) pada {record.date}',
                'content': record.description,
                'blog_id': blog.id,
                'author_id': author_id,
                'is_published': True,
            })

    def action_reject(self):
        for record in self:
            record.state = 'rejected'
