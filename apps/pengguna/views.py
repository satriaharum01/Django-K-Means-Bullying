import os
from django import template
from django.core import serializers
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, Http404

#Decorators
from ..decorators import admin_required

# Models Import
from django.contrib.auth.models import User

# import class Form dari file forms.py
from .forms import PenggunaForm

# Create your views here.

@admin_required
def index(request):
    title = "Data Pengguna"
    page = "kuesioner"
    data = User.objects.prefetch_related('groups').all()
    form = PenggunaForm()
    context = {"data": data, "page": page, "title": title,"form":form}

    html_template = loader.get_template("page/pengguna.html")
    return HttpResponse(html_template.render(context, request))

# STORE
def create(request):
    if request.method == 'POST':
        form = PenggunaForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sukses tambah data.')
            return redirect('pengguna')
        else:
            messages.error(request, "Failed to create user. Please check the form for errors.")
            
            title = "Data Pengguna"
            page = "kuesioner"
            data = User.objects.prefetch_related('groups').all()
            context = {"data": data, "page": page, "title": title,"form":form}
            
            html_template = loader.get_template("page/pengguna.html")
            return HttpResponse(html_template.render(context, request))
    else:
        return redirect('pengguna')

# UPDATE
def update(request, data_id):
    all_objs = User.objects.get(id=data_id)
    if request.method == 'POST':
        form = PenggunaForm(request.POST, instance=all_objs)
        if form.is_valid():
            form.save()
            
            messages.success(request, 'Sukses update data.')
            return redirect('pengguna')
    # Jika method-nya bukan POST
    else:
        return redirect('pengguna')
    
# DESTROY
def delete(request, data_id):
    try:
        all_objs = User.objects.get(id=data_id)
        all_objs.delete()
        return redirect('pengguna')
    except User.DoesNotExist:
        raise Http404("Task tidak ditemukan.")

# JSON DATA OBJECT
def json(request):
    if request.method == "GET":
        users  = User.objects.prefetch_related('groups').all().order_by('username')
        user_data = []
        i=1
        for user in users:
            group_name = user.groups.first().name if user.groups.exists() else None
            DT_RowIndex=i
            user_data.append({
                'DT_RowIndex': DT_RowIndex,
                'username': user.username,
                'email': user.email,
                'group_name': group_name,
                'first_name': user.first_name,
                'last_name': user.last_name,
            })
            i= i+1
            #for i in load.items():
            #    load.items
        data = {"data": user_data}
        return JsonResponse(data, safe=False)
    else:
        messages.success(request, 'Invalid Method')
        return redirect('kuesioner')
    
# FIND DATA OBJECT
def find(request, data_id):
    if request.method == "GET":
        all_objs = User.objects.all().values("id","question_text","question_type").filter(id=data_id)
        print(all_objs)
        data = {"data": list(all_objs)}
        return JsonResponse(data, safe=False)
    else:
        messages.success(request, 'Invalid Method')
        return redirect('pengguna')