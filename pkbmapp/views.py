from django.shortcuts import render, get_object_or_404
from .models import Galeri, Berita
from django.core.paginator import Paginator



def home(request):
    return render(request, 'pkbmapp/home.html')

def profil(request):
    return render(request, 'pkbmapp/profil.html')

def program(request):
    return render(request, 'pkbmapp/program.html')

def kontak(request):
    return render(request, 'pkbmapp/kontak.html')


def berita(request):
    berita_all = Berita.objects.all()
    paginator = Paginator(berita_all, 6)  # 6 berita per halaman
    page_number = request.GET.get('page')
    berita_page = paginator.get_page(page_number)
    
    featured = berita_all.first()
    return render(request, 'pkbmapp/berita.html', {
        'featured': featured,
        'berita_page': berita_page,
    })

def berita_detail(request, slug):
    berita = get_object_or_404(Berita, slug=slug)
    return render(request, 'pkbmapp/berita_detail.html', {'berita': berita})

def galeri(request):
    galeri_per_bulan = {}
    for bulan, nama in Galeri.BULAN_CHOICES:
        galeri_per_bulan[nama] = Galeri.objects.filter(bulan=bulan)
    return render(request, 'pkbmapp/galeri.html', {'galeri_per_bulan': galeri_per_bulan})
