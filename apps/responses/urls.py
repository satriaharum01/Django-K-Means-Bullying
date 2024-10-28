from django.urls import path, re_path
from . import views

urlpatterns = [
    path('kuesioner/', views.index, name='siswa/kuesioner'),
    path('kuesioner/isi/<int:data_id>', views.isi, name="siswa/kuesioner/isi"),
    path('kuesioner/json', views.json, name="siswa/kuesioner/json"),
    path('kuesioner/find/<int:data_id>', views.find, name="siswa/kuesioner/find"),
]
