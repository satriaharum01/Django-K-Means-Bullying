from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('peramalan/', views.index, name='peramalan'),
    path('guru/peramalan/', views.index_guru, name='guru/peramalan')
]

# Menyajikan file media saat dalam mode pengembangan
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)