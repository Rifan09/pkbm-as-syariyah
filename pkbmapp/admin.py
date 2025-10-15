from django.contrib import admin
from .models import Program, Pendaftar, Galeri

class PendaftarAdmin(admin.ModelAdmin):
    """Kustomisasi tampilan Pendaftar di halaman admin."""
    list_display = ('nama_lengkap', 'program_pilihan', 'email', 'tanggal_pendaftaran')
    list_filter = ('program_pilihan', 'tanggal_pendaftaran')
    search_fields = ('nama_lengkap', 'email')

# Daftarkan model dan kustomisasi adminnya
admin.site.register(Program)
admin.site.register(Pendaftar, PendaftarAdmin)

class GaleriAdmin(admin.ModelAdmin):
    list_display = ('judul', 'get_bulan_display', 'tanggal_upload', 'preview_image')
    list_filter = ('bulan', 'tanggal_upload')
    search_fields = ('judul', 'deskripsi')
    readonly_fields = ('preview_image', 'tanggal_upload')

    fieldsets = (
        ('Informasi Foto', {
            'fields': ('judul', 'deskripsi', 'foto', 'preview_image')
        }),
        ('Informasi Waktu', {
            'fields': ('bulan', 'tanggal_upload')
        }),
    )

    def preview_image(self, obj):
        """Menampilkan thumbnail kecil di admin."""
        if obj.foto:
            return format_html('<img src="{}" width="150" height="100" style="object-fit:cover; border-radius:8px;"/>', obj.foto.url)
        return "(Belum ada foto)"
    preview_image.short_description = "Preview Foto"

admin.site.register(Galeri)


