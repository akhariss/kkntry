# -*- coding: utf-8 -*-
{
    'name': 'TIPD KKN Management',
    'version': '1.0',
    'category': 'Education/KKN',
    'summary': 'Modul untuk Manajemen Kuliah Kerja Nyata (KKN)',
    'description': """
        Sistem Manajemen KKN meliputi:
        - Pengelolaan Program / Periode KKN
        - Pengelolaan Kelompok & Posko
        - Pendaftaran & Pendataan Mahasiswa (Peserta)
        - Dosen Pembimbing Lapangan (DPL)
        - Logbook / Laporan Kegiatan Harian (LKH)
        - Penilaian
    """,
    'author': 'SufyALDI - Forum TIPD',
    'website': '',
    'depends': ['base', 'mail'],
    'data': [
        'security/kkn_security.xml',
        'security/ir.model.access.csv',
        'views/kkn_program_views.xml',
        'views/kkn_location_views.xml',
        'views/kkn_group_views.xml',
        'views/kkn_participant_views.xml',
        'views/kkn_supervisor_views.xml',
        'views/kkn_activity_views.xml',
        'views/kkn_grade_views.xml',
        'views/kkn_menus.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
