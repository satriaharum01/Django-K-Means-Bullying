from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='dashboard'),
    path('dashboard/', views.index, name='dashboard')
]
