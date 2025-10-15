from django import forms
from .models import PendaftaranSiswa

class BiodataForm(forms.ModelForm):
    class Meta:
        model = PendaftaranSiswa
        fields = [
            'nama_lengkap', 'tanggal_lahir', 'alamat',
            'nomor_telepon', 'email', 'program_pilihan'
        ]
        widgets = {
            'nama_lengkap': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nama lengkap Anda'}),
            'tanggal_lahir': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'alamat': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'nomor_telepon': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'program_pilihan': forms.Select(attrs={'class': 'form-select'}),
        }

class DokumenForm(forms.ModelForm):
    class Meta:
        model = PendaftaranSiswa
        fields = [
            'foto_diri', 'fotocopy_ijazah', 'kartu_keluarga',
            'bukti_pembayaran', 'rapor_sekolah', 'surat_keterangan_sekolah'
        ]
        widgets = {
            field: forms.ClearableFileInput(attrs={'class': 'form-control'})
            for field in fields
        }
