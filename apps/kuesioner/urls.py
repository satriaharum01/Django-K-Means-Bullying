from django.urls import path, re_path
from . import views

urlpatterns = [
    path('kuesioner/', views.index, name='kuesioner'),
    path('kuesioner/save', views.create, name='kuesioner/save'),
    path('kuesioner/update/<int:data_id>', views.update, name="kuesioner/update"),
    path('kuesioner/delete/<int:data_id>', views.delete, name="kuesioner/delete"),
    path('kuesioner/json', views.json, name="kuesioner/json"),
    path('kuesioner/find/<int:data_id>', views.find, name="kuesioner/find"),
]
