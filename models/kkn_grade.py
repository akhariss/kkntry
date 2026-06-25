# -*- coding: utf-8 -*-
from odoo import models, fields

class KknGrade(models.Model):
    _name = 'tipd_kkn.grade'
    _description = 'Penilaian Mahasiswa'
    _inherit = ['mail.thread']

    participant_id = fields.Many2one('tipd_kkn.participant', string='Mahasiswa', required=True, tracking=True)
    supervisor_id = fields.Many2one('tipd_kkn.supervisor', string='Penilai (DPL)', required=True, tracking=True)
    
    score = fields.Float(string='Nilai Akhir', required=True, tracking=True)
    grade_letter = fields.Char(string='Huruf Mutu', compute='_compute_grade_letter', store=True)
    
    notes = fields.Text(string='Catatan Penilaian')

    def _compute_grade_letter(self):
        for record in self:
            if record.score >= 85:
                record.grade_letter = 'A'
            elif record.score >= 70:
                record.grade_letter = 'B'
            elif record.score >= 55:
                record.grade_letter = 'C'
            elif record.score >= 40:
                record.grade_letter = 'D'
            else:
                record.grade_letter = 'E'
