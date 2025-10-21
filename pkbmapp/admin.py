from django.contrib import admin
from .models import Program, Pendaftar, Galeri, Berita, MasukanSaran, Profil
from django.utils.html import format_html

class PendaftarAdmin(admin.ModelAdmin):
    """Kustomisasi tampilan Pendaftar di halaman admin."""
    list_display = ('nama_lengkap', 'program_pilihan', 'email', 'tanggal_pendaftaran')
    list_filter = ('program_pilihan', 'tanggal_pendaftaran')
    search_fields = ('nama_lengkap', 'email')

# Daftarkan model dan kustomisasi adminnya
admin.site.register(Program)
admin.site.register(Pendaftar, PendaftarAdmin)
admin.site.register(Profil)

@admin.register(Galeri)
class GaleriAdmin(admin.ModelAdmin):
    list_display = ('judul', 'get_bulan_display', 'tanggal_upload', 'preview_media')
    list_filter = ('bulan', 'tanggal_upload')
    search_fields = ('judul', 'deskripsi')
    readonly_fields = ('preview_media', 'tanggal_upload')

    fieldsets = (
        ('Informasi Media', {
            'fields': ('judul', 'deskripsi', 'foto', 'video_url', 'video_file', 'preview_media')
        }),
        ('Informasi Waktu', {
            'fields': ('bulan', 'tanggal_upload')
        }),
    )

    def preview_media(self, obj):
        """
        Menampilkan preview gambar atau video (lokal/link) di admin.
        """
        if obj.foto:
            return format_html(
                '<img src="{}" width="200" height="120" style="object-fit:cover; border-radius:8px;"/>',
                obj.foto.url
            )
        elif obj.video_file:
            return format_html(
                '<video width="200" height="120" controls style="border-radius:8px; object-fit:cover;">'
                '<source src="{}" type="video/mp4">'
                'Browser Anda tidak mendukung video.'
                '</video>',
                obj.video_file.url
            )
        elif obj.video_url:
            # embed otomatis untuk YouTube atau Facebook
            if "youtube.com" in obj.video_url or "youtu.be" in obj.video_url:
                return format_html(
                    '<iframe width="200" height="120" src="{}" frameborder="0" allowfullscreen></iframe>',
                    obj.video_url.replace("watch?v=", "embed/")
                )
            elif "facebook.com" in obj.video_url:
                return format_html(
                    '<iframe src="{}" width="200" height="120" style="border:none;overflow:hidden" '
                    'scrolling="no" frameborder="0" allowfullscreen="true"></iframe>',
                    obj.video_url
                )
        return "(Belum ada media)"
    preview_media.short_description = "Preview Media"

@admin.register(Berita)
class BeritaAdmin(admin.ModelAdmin):
    list_display = ('judul', 'kategori', 'penulis', 'tanggal_publikasi')
    prepopulated_fields = {'slug': ('judul',)}

@admin.register(MasukanSaran)
class MasukanSaranAdmin(admin.ModelAdmin):
    list_display = ('nama', 'email', 'subjek', 'tanggal_kirim')
    search_fields = ('nama', 'email', 'subjek')
    readonly_fields = ('tanggal_kirim',)
