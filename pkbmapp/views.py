from django.shortcuts import render, get_object_or_404, redirect
from .models import Galeri, Berita, Profil
from django.core.paginator import Paginator
from django.contrib import messages
from .forms import MasukanSaranForm



def home(request):
    # Ambil 4 berita terakhir berdasarkan tanggal publikasi
    berita_terbaru = Berita.objects.all().order_by('-tanggal_publikasi')[:4]
    context = {
        'berita_terbaru': berita_terbaru,
    }
    return render(request, 'pkbmapp/home.html', context)

def profil(request):
    ptk_list = Profil.objects.all()
    return render(request, "pkbmapp/profil.html", {"ptk_list": ptk_list})

def program(request):
    return render(request, 'pkbmapp/program.html')

def paket_a(request):
    return render(request, 'pkbmapp/paket_a.html')

def paket_b(request):
    return render(request, 'pkbmapp/paket_b.html')

def paket_c(request):
    return render(request, 'pkbmapp/paket_c.html')


def kontak(request):
    if request.method == 'POST':
        form = MasukanSaranForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Pesan Anda telah terkirim. Terima kasih atas masukannya!")
            return redirect('kontak')
    else:
        form = MasukanSaranForm()

    return render(request, 'pkbmapp/kontak.html', {'form': form})

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
