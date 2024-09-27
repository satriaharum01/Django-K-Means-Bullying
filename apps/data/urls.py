from django.urls import path, re_path
from . import views

urlpatterns = [
    path('data/', views.index, name='data'),
    path('data/save', views.create, name='data/save'),
    path('data/update/<int:data_id>', views.update, name="data/update"),
    path('data/delete/<int:data_id>', views.delete, name="data/delete"),
    path('data/json', views.json, name="data/json"),
    path('data/find/<int:data_id>', views.find, name="data/find"),
]
