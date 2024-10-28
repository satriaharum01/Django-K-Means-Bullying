import os
from django import template
from django.core import serializers
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, Http404

#Decorators
from ..decorators import siswa_required

# Models Import
from ..models import m_kuesioner, m_response

# import class Form dari file forms.py
from .forms import ResponsesForm

# Create your views here.

@siswa_required
def index(request):
    title = "Data Kuesioner"
    page = "kuesioner"
    data = m_kuesioner.objects.all()
    form = ResponsesForm()
    context = {"data": data, "page": page, "title": title,"form":form}

    html_template = loader.get_template("page/responses.html")
    return HttpResponse(html_template.render(context, request))


# Isi Kuesioner
def isi(request, data_id):
    auth_id = request.user.id
    # Ambil kuesioner yang dimaksud
    kuesioner = m_kuesioner.objects.get(id=data_id)
    
    # Coba ambil respons yang sudah ada untuk user ini dan kuesioner ini
    try:
        response = m_response.objects.get(user_id=auth_id, kuesioner=kuesioner)
    except m_response.DoesNotExist:
        response = None  # Jika tidak ada respons, kita akan buat yang baru
    
    if request.method == 'POST':
        form = ResponsesForm(request.POST, instance=response)
        print(form)
        if form.is_valid():
            response = form.save(commit=False)  # Tidak simpan ke database dulu
            response.user_id = auth_id  # Set user dari parameter
            response.save()  # Simpan ke database
            messages.success(request, 'Sukses Isi Kuesioner.')
            return redirect('siswa/kuesioner')
        else:
            return redirect('siswa/kuesioner')
    # Jika method-nya bukan POST
    else:
        return redirect('siswa/kuesioner')

# JSON DATA OBJECT
def json(request):
    auth_id = request.user.id
    
    RESPONSES_TYPES = [
        'Belum Dijawab',
        'Sangat Jarang',
        'Jarang',
        'Kadang Kadang',
        'Sering',
        'Sangat Sering',
    ]
    if request.method == "GET":
        all_objs = m_kuesioner.objects.all().order_by('question_type').values("id","question_text","question_type")
        i=1
        for load in all_objs:
            kuesioner = m_kuesioner.objects.get(id=load['id'])
            response = m_response.objects.filter(user_id=auth_id, kuesioner=kuesioner).first()
            load['DT_RowIndex']=i
            print(response)
            if not response:
                load['answer'] = RESPONSES_TYPES[0]
            else:   
                load['answer'] = RESPONSES_TYPES[response.answer]
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
        all_objs = m_kuesioner.objects.all().values("id").filter(id=data_id)
        for load in all_objs:
            response = m_response.objects.filter(id=load['id']).values("id","kuesioner_id","answer","submission_date")
            load['kuesioner'] = load['id']
            if not response:
                load['answer'] = 0
            else:   
                load['answer'] = response[0]['answer']
                
        data = {"data": list(all_objs)}
        return JsonResponse(data, safe=False)
    else:
        messages.success(request, 'Invalid Method')
        return redirect('kuesioner')