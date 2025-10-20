from django import forms
from .models import Pendaftar, MasukanSaran

class PendaftaranForm(forms.ModelForm):
    class Meta:
        model = Pendaftar
        fields = [
            'nama_lengkap', 
            'tanggal_lahir', 
            'alamat', 
            'nomor_telepon', 
            'email', 
            'program_pilihan'
        ]
        widgets = {
            'nama_lengkap': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Masukkan nama lengkap Anda'
            }),
            'tanggal_lahir': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'alamat': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Masukkan alamat lengkap Anda'
            }),
            'nomor_telepon': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Contoh: 081234567890'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'contoh@email.com'
            }),
            'program_pilihan': forms.Select(attrs={
                'class': 'form-select'
            }),
        }
        labels = {
            'program_pilihan': 'Pilih Program Belajar'
        }


class MasukanSaranForm(forms.ModelForm):
    class Meta:
        model = MasukanSaran
        fields = ['nama', 'email', 'subjek', 'pesan']
        widgets = {
            'nama': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nama Lengkap Anda',
                'required': True
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Alamat Email',
                'required': True
            }),
            'subjek': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Subjek Pesan',
                'required': True
            }),
            'pesan': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Tulis pesan atau saran Anda di sini...',
                'rows': 5,
                'required': True
            }),
        }


