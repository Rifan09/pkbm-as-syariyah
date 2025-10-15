from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import BiodataForm, DokumenForm

def pendaftaran(request):
    return render(request, 'pendaftaran/detail-pendaftaran.html')

def pendaftaran_step1(request):
    if request.method == 'POST':
        form = BiodataForm(request.POST)
        if form.is_valid():
            biodata = form.cleaned_data.copy()
            if 'tanggal_lahir' in biodata and hasattr(biodata['tanggal_lahir'], 'isoformat'):
                biodata['tanggal_lahir'] = biodata['tanggal_lahir'].isoformat()
            request.session['biodata'] = biodata
            return redirect('pendaftaran_step2')
    else:
        form = BiodataForm()
    return render(request, 'pendaftaran/pendaftaran_step1.html', {'form': form})

def pendaftaran_step2(request):
    biodata = request.session.get('biodata')
    if not biodata:
        return redirect('pendaftaran_step1')

    if request.method == 'POST':
        form = DokumenForm(request.POST, request.FILES)
        if form.is_valid():
            pendaftar = form.save(commit=False)
            for key, value in biodata.items():
                setattr(pendaftar, key, value)
            pendaftar.save()
            # bersihkan session
            del request.session['biodata']
            return redirect('pendaftaran_sukses')
    else:
        form = DokumenForm()
    return render(request, 'pendaftaran/step2_dokumen.html', {'form': form})

# @login_required
def sukses(request):
    return render(request, 'pendaftaran/form_sukses.html')

