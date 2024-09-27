from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.dashboard.urls')),
    path('', include('myauth.urls')),
    path('', include('apps.data.urls')),
    path('', include('apps.peramalan.urls'))
]