from django.contrib import admin

from .models import m_data,m_kuesioner,m_response
# Register your models here.
admin.site.register(m_data)
admin.site.register(m_kuesioner)
admin.site.register(m_response)