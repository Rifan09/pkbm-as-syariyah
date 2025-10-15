from django.urls import path
from  .import views

urlpatterns = [
    path('detail-pendaftaran/', views.pendaftaran, name='pendaftaran'),
    path('pendaftaran/step1/', views.pendaftaran_step1, name='pendaftaran_step1'),
    path('pendaftaran/step2/', views.pendaftaran_step2, name='pendaftaran_step2'),
    path('pendaftaran/sukses/', views.sukses, name='pendaftaran_sukses'),
]