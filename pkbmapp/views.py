from django.shortcuts import render
from .models import Galeri



def home(request):
    return render(request, 'pkbmapp/home.html')

def profil(request):
    return render(request, 'pkbmapp/profil.html')

def program(request):
    return render(request, 'pkbmapp/program.html')

def berita(request):
    return render(request, 'pkbmapp/berita.html')

def kontak(request):
    return render(request, 'pkbmapp/kontak.html')


def galeri(request):
    galeri_per_bulan = {}
    for bulan, nama in Galeri.BULAN_CHOICES:
        galeri_per_bulan[nama] = Galeri.objects.filter(bulan=bulan)
    return render(request, 'pkbmapp/galeri.html', {'galeri_per_bulan': galeri_per_bulan})
