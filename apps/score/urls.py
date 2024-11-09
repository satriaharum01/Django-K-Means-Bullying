from django.urls import path, re_path
from . import views

urlpatterns = [
    path('score/', views.index, name='score'),
    path('score/json', views.json, name="score/json"),
    path('score/find/<int:data_id>', views.find, name="score/find"),
]
