from django.db import models
from django.utils.text import slugify

class Program(models.Model):
    """Model untuk program belajar yang ditawarkan PKBM."""
    nama = models.CharField(max_length=100, help_text="Contoh: Paket C Setara SMA")
    deskripsi = models.TextField()

    def __str__(self):
        return self.nama


class Pendaftar(models.Model):
    """Model untuk menyimpan data siswa yang mendaftar."""
    nama_lengkap = models.CharField(max_length=150)
    tanggal_lahir = models.DateField()
    alamat = models.TextField()
    nomor_telepon = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    
    # Relasi ke Program: Setiap pendaftar memilih satu program.
    # Jika program dihapus, data pendaftar terkait juga akan terhapus (CASCADE).
    program_pilihan = models.ForeignKey(Program, on_delete=models.CASCADE)
    
    tanggal_pendaftaran = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nama_lengkap} - {self.program_pilihan.nama}"
    
class Galeri(models.Model):
    BULAN_CHOICES = [
        ('01', 'Januari'), ('02', 'Februari'), ('03', 'Maret'),
        ('04', 'April'), ('05', 'Mei'), ('06', 'Juni'),
        ('07', 'Juli'), ('08', 'Agustus'), ('09', 'September'),
        ('10', 'Oktober'), ('11', 'November'), ('12', 'Desember'),
    ]
    judul = models.CharField(max_length=100)
    deskripsi = models.TextField(blank=True)
    foto = models.ImageField(upload_to='galeri/')
    video_url = models.URLField(blank=True, null=True, help_text="Masukkan URL video Facebook atau YouTube (opsional)")
    video_file = models.FileField(upload_to='galeri/video/', blank=True, null=True, help_text="Upload video lokal (mp4/mov)")
    tanggal_upload = models.DateTimeField(auto_now_add=True)
    bulan = models.CharField(max_length=2, choices=BULAN_CHOICES, blank=True)

    def save(self, *args, **kwargs):
        if not self.bulan and self.tanggal_upload:
            self.bulan = self.tanggal_upload.strftime('%m')
        super().save(*args, **kwargs)


class Berita(models.Model):
    judul = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    kategori = models.CharField(max_length=100)
    isi = models.TextField()
    gambar = models.ImageField(upload_to='berita/')
    penulis = models.CharField(max_length=100, default="Admin")
    tanggal_publikasi = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-tanggal_publikasi']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.judul)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.judul


class MasukanSaran(models.Model):
    nama = models.CharField(max_length=100)
    email = models.EmailField()
    subjek = models.CharField(max_length=150)
    pesan = models.TextField()
    tanggal_kirim = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nama} - {self.subjek}"
