from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profil/', views.profil, name='profil'),
    path('program/', views.program, name='program'),
    path('berita/', views.berita, name='berita'),
    path('berita/<slug:slug>/', views.berita_detail, name='berita_detail'),
    path('galeri/', views.galeri, name='galeri'),
    path('kontak/', views.kontak, name='kontak'),
]