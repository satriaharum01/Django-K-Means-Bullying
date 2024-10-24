import os
from django import template
from django.core import serializers
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, Http404

# Models Import

from ..models import m_kuesioner

# import class Form dari file forms.py
from .forms import KuesionerForm

# Create your views here.

@login_required(login_url="/login/")
def index(request):
    title = "Data Kuesioner"
    page = "kuesioner"
    data = m_kuesioner.objects.all()
    form = KuesionerForm()
    context = {"data": data, "page": page, "title": title,"form":form}

    html_template = loader.get_template("page/kuesioner.html")
    return HttpResponse(html_template.render(context, request))

# STORE
def create(request):
    if request.method == 'POST':
        form = KuesionerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sukses tambah data.')
            return redirect('kuesioner')
    else:
        return redirect('kuesioner')

# UPDATE
def update(request, data_id):
    all_objs = m_kuesioner.objects.get(id=data_id)
    if request.method == 'POST':
        form = KuesionerForm(request.POST, instance=all_objs)
        if form.is_valid():
            form.save()
            
            messages.success(request, 'Sukses update data.')
            return redirect('kuesioner')
    # Jika method-nya bukan POST
    else:
        return redirect('kuesioner')
    
# DESTROY
def delete(request, data_id):
    try:
        all_objs = m_kuesioner.objects.get(id=data_id)
        all_objs.delete()
        return redirect('kuesioner')
    except m_kuesioner.DoesNotExist:
        raise Http404("Task tidak ditemukan.")

# JSON DATA OBJECT
def json(request):
    if request.method == "GET":
        all_objs = m_kuesioner.objects.all().order_by('question_type').values("id","question_text","question_type")
        i=1
        for load in all_objs:
            load['DT_RowIndex']=i
            i= i+1
            #for i in load.items():
            #    load.items
        data = {"data": list(all_objs)}
        return JsonResponse(data, safe=False)
    else:
        messages.success(request, 'Invalid Method')
        return redirect('kuesioner')
    
# FIND DATA OBJECT
def find(request, data_id):
    if request.method == "GET":
        all_objs = m_kuesioner.objects.all().values("id","question_text","question_type").filter(id=data_id)
        print(all_objs)
        data = {"data": list(all_objs)}
        return JsonResponse(data, safe=False)
    else:
        messages.success(request, 'Invalid Method')
        return redirect('kuesioner')