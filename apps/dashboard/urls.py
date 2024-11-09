from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='dashboard'),
    path('pusat/dashboard/', views.index, name='admin/dashboard'),
    path('pusat/dashboard/', views.index, name='pusat/dashboard'),
    path('guru/dashboard/', views.guru, name='guru/dashboard'),
    path('siswa/dashboard/', views.siswa, name='siswa/dashboard')
]
