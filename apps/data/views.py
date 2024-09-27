import os
from django import template
from django.core import serializers
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, Http404

# Models Import

from ..models import m_data

# import class Form dari file forms.py
from .forms import DataForm

month = ['','Januari','Febuari','Maret','April','Mei','Juni','Juli','Agustus','September','Oktober','November','Desember']
# Create your views here.

@login_required(login_url="/login/")
def index(request):
    title = "Data History"
    page = "data"
    data = m_data.objects.all()
    context = {"data": data, "page": page, "title": title}

    html_template = loader.get_template("page/data.html")
    return HttpResponse(html_template.render(context, request))

# STORE
def create(request):
    # Mengecek method pada request
    # Jika method-nya adalah POST, maka akan dijalankan
    # proses validasi dan penyimpanan data
    if request.method == 'POST':
        # membuat objek dari class Form
        form = DataForm(request.POST)
        # Mengecek validasi form
        if form.is_valid():
            # Membuat Form baru dengan data yang disubmit
            new_task = DataForm(request.POST)
            
            # Simpan data ke dalam table
            new_task.save()
            
            messages.success(request, 'Sukses Menambah Data baru.')
            return redirect('data')
    # Jika method-nya bukan POST
    else:
        
        return redirect('data')

# UPDATE
def update(request, data_id):
    # Mengecek method pada request
    # Jika method-nya adalah POST, maka akan dijalankan
    # proses validasi dan penyimpanan data
    all_objs = m_data.objects.get(id=data_id)
    if request.method == 'POST':
        # membuat objek dari class Form
        form = DataForm(request.POST, instance=all_objs)
        # Mengecek validasi form
        if form.is_valid():
            # Simpan data ke dalam table
            form.save()
            
            messages.success(request, 'Sukses update data.')
            return redirect('data')
    # Jika method-nya bukan POST
    else:
        return redirect('data')
    
# DESTROY
def delete(request, data_id):
    try:
        all_objs = m_data.objects.get(id=data_id)
        all_objs.delete()
        return redirect('data')
    except m_data.DoesNotExist:
        raise Http404("Task tidak ditemukan.")

# JSON DATA OBJECT
def json(request):
    if request.method == "GET":
        results = []
        all_objs = m_data.objects.all().order_by('-periode').values("id","jumlah","periode","ekspor")
        i=1
        for load in all_objs:
            periode = load['periode']
            load['DT_RowIndex']=i
            load['bulan']= int(periode[5:7])
            load['periode'] = month[load['bulan']] +' '+ load['periode'][0:4]
            i= i+1
            #for i in load.items():
            #    load.items
        data = {"data": list(all_objs)}
        return JsonResponse(data, safe=False)
    
# FIND DATA OBJECT
def find(request, data_id):
    
    all_objs = m_data.objects.all().values("id","jumlah","periode","ekspor").filter(id=data_id)
    print(all_objs)
    data = {"data": list(all_objs)}
    return JsonResponse(data, safe=False)