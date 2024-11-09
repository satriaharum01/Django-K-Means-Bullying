import os
from django import template
from django.core import serializers
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

# Models Import
from django.contrib.auth.models import User
from ..models import m_data, m_kuesioner, m_response
from ..decorators import admin_required, siswa_required, guru_bk_required

# Create your views here.
@login_required
@admin_required
def index(request):
    data = {}
    data['siswa'] = User.objects.filter(groups__name='Siswa').count()
    data['kuesioner'] = m_kuesioner.objects.count()
    data['jawaban'] = m_response.objects.count()
    
    context = {"segment": "dashboard","value": data}

    html_template = loader.get_template("page/dashboard.html")
    return HttpResponse(html_template.render(context, request))


@login_required
@guru_bk_required
def guru(request):
    data = {}
    data['siswa'] = User.objects.filter(groups__name='Siswa').count()
    data['kuesioner'] = m_kuesioner.objects.count()
    data['jawaban'] = m_response.objects.count()
    
    context = {"segment": "dashboard","value": data}

    html_template = loader.get_template("page/dashboard.html")
    return HttpResponse(html_template.render(context, request))

@login_required
@siswa_required
def siswa(request):
    
    auth_id = request.user.id
    data = {}
    siswa = User.objects.prefetch_related('groups').all().filter(id=auth_id)
    
    for student in siswa:
        full_name = f"{student.first_name} {student.last_name}"
        
    data['siswa'] = full_name
    data['kuesioner'] = m_kuesioner.objects.count()
    data['jawaban'] = m_response.objects.filter(user=request.user).count()
    
    context = {"segment": "dashboard","value": data}

    html_template = loader.get_template("page/dashboard.html")
    return HttpResponse(html_template.render(context, request))