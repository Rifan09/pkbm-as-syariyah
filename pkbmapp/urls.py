from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profil/', views.profil, name='profil'),
    path('program/', views.program, name='program'),
    path('program/paket-a/', views.paket_a, name='paket_a'),
    path('program/paket-b/', views.paket_b, name='paket_b'),
    path('program/paket-c/', views.paket_c, name='paket_c'),
    path('berita/', views.berita, name='berita'),
    path('berita/<slug:slug>/', views.berita_detail, name='berita_detail'),
    path('galeri/', views.galeri, name='galeri'),
    path('kontak/', views.kontak, name='kontak'),
]