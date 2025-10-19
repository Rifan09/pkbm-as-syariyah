# app_name/models.py
from django.db import models

class PendaftaranSiswa(models.Model):
    PROGRAM_CHOICES = [
        ('paket_a', 'Paket A (SD Sederajat)'),
        ('paket_b', 'Paket B (SMP Sederajat)'),
        ('paket_c', 'Paket C (SMA Sederajat)'),
    ]

    nama_lengkap = models.CharField(max_length=100)
    tempat_lahir = models.CharField(max_length=50)
    tanggal_lahir = models.DateField()
    alamat = models.TextField()
    nomor_telepon = models.CharField(max_length=15)
    email = models.EmailField()
    sekolah_asal = models.CharField(max_length=100)
    program_pilihan = models.CharField(max_length=20, choices=PROGRAM_CHOICES)

    # File upload fields
    foto_diri = models.ImageField(upload_to='pendaftaran/foto_diri/')
    fotocopy_ijazah = models.FileField(upload_to='pendaftaran/ijazah/')
    kartu_keluarga = models.FileField(upload_to='pendaftaran/kk/')
    bukti_pembayaran = models.FileField(upload_to='pendaftaran/bukti/')
    rapor_sekolah = models.FileField(upload_to='pendaftaran/rapor/')
    surat_keterangan_sekolah = models.FileField(upload_to='pendaftaran/surat/')

    tanggal_daftar = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nama_lengkap} - {self.get_program_pilihan_display()}"
