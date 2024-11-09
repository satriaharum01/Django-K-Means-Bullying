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
from django.contrib.auth.models import User, Group

# import class Form dari file forms.py
from .forms import PenggunaForm

# Create your views here.

@admin_required
def index(request):
    title = "Data Pengguna"
    page = "kuesioner"
    data = User.objects.prefetch_related('groups').all()
    form = PenggunaForm()
    passform = PenggunaForm()
    context = {"data": data, "page": page, "title": title,"form":form,"passform":passform}

    html_template = loader.get_template("page/pengguna.html")
    return HttpResponse(html_template.render(context, request))

# STORE
def create(request):
    if request.method == 'POST':
        form = PenggunaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sukses tambah data.')
            return redirect('pengguna')
        else:
            messages.error(request, "Failed to create user. Please check the form for errors.")
            
            title = "Data Pengguna"
            page = "kuesioner"
            data = User.objects.prefetch_related('groups').all()
            context = {"data": data, "page": page, "title": title,"form":form,"err_page": 'error'}
            
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
            password1 = form.cleaned_data['password1']
            if password1:
                form.save()
                messages.success(request, 'Sukses update data.')
                return redirect('pengguna')
            else:
                User.objects.filter(pk=data_id).update(
                    username=form.cleaned_data['username'],
                    email=form.cleaned_data['email'],
                    first_name=form.cleaned_data['first_name'],
                    last_name=form.cleaned_data['last_name']
                )
                user = User.objects.get(pk=data_id)
                user.groups.clear()
                new_group_name = form.cleaned_data.get('role')  # Assuming 'role' corresponds to a group name

                if new_group_name:
                    user.groups.add(new_group_name)
                    
                return redirect('pengguna')
        else:
            messages.error(request, "Failed to create user. Please check the form for errors.")
            title = "Data Pengguna"
            page = "kuesioner"
            data = User.objects.prefetch_related('groups').all()
            context = {"data": data, "page": page, "title": title,"form":form,"err_page": 'error'}
            html_template = loader.get_template("page/pengguna.html")
            return HttpResponse(html_template.render(context, request))
        
            
        
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
                'id': user.id,
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
        messages.error(request, 'Invalid Method')
        return redirect('kuesioner')
    
# FIND DATA OBJECT
def find(request, data_id):
    if request.method == "GET":
        users = User.objects.prefetch_related('groups').all().filter(id=data_id)
        user_data = []
        for user in users:
            group_id = user.groups.first().id if user.groups.exists() else None
            user_data.append({
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'role': group_id,
                'first_name': user.first_name,
                'last_name': user.last_name,
            })
        data = {"data": list(user_data)}
        return JsonResponse(data, safe=False)
    else:
        messages.error(request, 'Invalid Method')
        return redirect('pengguna')