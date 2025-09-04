"""
URL configuration for pkbm project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from pkbmapp import views



urlpatterns = [
    path('admin/', admin.site.urls),
    
   # profiles sebagai root
    path('', include('pkbmapp.urls')),

#     # UI Publik
#     path('sekolah/', views.sekolah_detail, name="sekolah_detail"),
#     path('sekolah/edit/', views.sekolah_update, name="sekolah_update"),

#     path('program/', views.program_list, name="program_list"),
#     path('program/add/', views.program_create, name="program_create"),
#     path('program/<int:pk>/edit/', views.program_update, name="program_update"),
#     path('program/<int:pk>/delete/', views.program_delete, name="program_delete"),
]
