from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.dashboard.urls')),
    path('', include('myauth.urls')),
    path('pusat/', include('apps.data.urls')),
    path('pusat/', include('apps.kuesioner.urls')),
    path('pusat/', include('apps.pengguna.urls')),
    path('pusat/', include('apps.peramalan.urls')),
    path('siswa/', include('apps.responses.urls'))
]
