from django.contrib import admin
from .models import PendaftaranSiswa
from .admin_site import pendaftaran_admin_site

@admin.register(PendaftaranSiswa, site=pendaftaran_admin_site)
class PendaftaranSiswaAdmin(admin.ModelAdmin):
    list_display = ('nama_lengkap', 'program_pilihan', 'email', 'nomor_telepon', 'tanggal_daftar')
    list_filter = ('program_pilihan', 'tanggal_daftar')
    search_fields = ('nama_lengkap', 'email', 'sekolah_asal')
    readonly_fields = ('tanggal_daftar',)
    fieldsets = (
        ('Data Pribadi', {
            'fields': ('nama_lengkap', 'tempat_lahir', 'tanggal_lahir', 'alamat', 'nomor_telepon', 'email')
        }),
        ('Data Pendidikan', {
            'fields': ('sekolah_asal', 'program_pilihan')
        }),
        ('Berkas Pendaftaran', {
            'fields': ('foto_diri', 'fotocopy_ijazah', 'kartu_keluarga', 'bukti_pembayaran', 'rapor_sekolah', 'surat_keterangan_sekolah')
        }),
        ('Informasi Sistem', {
            'fields': ('tanggal_daftar',)
        }),
    )

