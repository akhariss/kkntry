# -*- coding: utf-8 -*-
from odoo import models, fields

class KknLocation(models.Model):
    _name = 'tipd_kkn.location'
    _description = 'Lokasi Posko KKN'

    name = fields.Char(string='Nama Posko / Lokasi', required=True, help="Contoh: Posko Desa Maju")
    village = fields.Char(string='Desa/Kelurahan')
    district = fields.Char(string='Kecamatan')
    regency = fields.Char(string='Kabupaten/Kota')
    province = fields.Char(string='Provinsi')
    address = fields.Text(string='Alamat Lengkap')
    latitude = fields.Float(string='Latitude', digits=(10, 7))
    longitude = fields.Float(string='Longitude', digits=(10, 7))

    group_ids = fields.One2many('tipd_kkn.group', 'location_id', string='Kelompok KKN')
