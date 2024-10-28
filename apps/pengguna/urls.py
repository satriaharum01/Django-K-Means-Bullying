from django.urls import path, re_path
from . import views

urlpatterns = [
    path('pengguna/', views.index, name='pengguna'),
    path('pengguna/save', views.create, name='pengguna/save'),
    path('pengguna/update/<int:data_id>', views.update, name="pengguna/update"),
    path('pengguna/delete/<int:data_id>', views.delete, name="pengguna/delete"),
    path('pengguna/json', views.json, name="pengguna/json"),
    path('pengguna/find/<int:data_id>', views.find, name="pengguna/find"),
]
