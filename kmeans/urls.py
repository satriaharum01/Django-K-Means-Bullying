from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.dashboard.urls')),
    path('', include('myauth.urls')),
    path('accounts/', include('myauth.urls')),
    path('pusat/', include('apps.kuesioner.urls')),
    path('pusat/', include('apps.pengguna.urls')),
    path('pusat/', include('apps.peramalan.urls')),
    path('pusat/', include('apps.score.urls')),
    path('siswa/', include('apps.responses.urls')),
    path('', include('apps.peramalan.urls')),
    path('', include('apps.score.urls')),
]
