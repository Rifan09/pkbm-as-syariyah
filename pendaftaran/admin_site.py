from django.contrib.admin import AdminSite

class PendaftaranAdminSite(AdminSite):
    site_header = "Pendaftaran PKBM As-Syari'yah"
    site_title = "Dashboard Pendaftaran"
    index_title = "Manajemen Data Siswa"

pendaftaran_admin_site = PendaftaranAdminSite(name='pendaftaran_admin')
