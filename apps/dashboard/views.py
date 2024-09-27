import os
from django import template
from django.core import serializers
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

# Models Import
from ..models import m_data

# Create your views here.


@login_required(login_url="/login/")
def index(request):
    data = {}
    data['dt_history'] = m_data.objects.count()
    data['dt'] = m_data.objects.all().order_by('-periode').values("id","jumlah","periode","ekspor").first()
    print(data['dt'])
    context = {"segment": "dashboard","value": data}

    html_template = loader.get_template("page/dashboard.html")
    return HttpResponse(html_template.render(context, request))
