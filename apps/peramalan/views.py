import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from django.db.models import Sum, Q
from django.template import loader
from django.http import HttpResponse
from django.conf import settings


#Decorators
from ..decorators import admin_required, guru_bk_required

# Models Import
from django.contrib.auth.models import User
from ..models import m_response,m_kuesioner
# Create your views here.

@admin_required
def index(request):
    
    students_scores = (
        User.objects.filter(groups__name='Siswa')
        .annotate(
            skor_fisik=Sum('m_response__answer', filter=Q(m_response__kuesioner__question_type='fisik')),
            skor_verbal=Sum('m_response__answer', filter=Q(m_response__kuesioner__question_type='verbal')),
            skor_psikologis=Sum('m_response__answer', filter=Q(m_response__kuesioner__question_type='psikologis'))
        )
    )
    
    # Format data ke bentuk dictionary
    data = {
        'ID Siswa': [],
        'Siswa': [],
        'Skor Fisik': [],
        'Skor Verbal': [],
        'Skor Psikologis': []
    }

    for student in students_scores:
        data['ID Siswa'].append(student.id)
        # Gabungkan first_name dan last_name
        full_name = f"{student.first_name} {student.last_name}"
        data['Siswa'].append(full_name)
        data['Skor Fisik'].append(student.skor_fisik or 0)
        data['Skor Verbal'].append(student.skor_verbal or 0)
        data['Skor Psikologis'].append(student.skor_psikologis or 0)
    
    # Membuat DataFrame
    df = pd.DataFrame(data)
    
    # Memilih kolom yang akan digunakan untuk clustering
    X = df[['Skor Fisik', 'Skor Verbal', 'Skor Psikologis']]
    
    # Menerapkan K-Means dengan 3 kluster
    kmeans = KMeans(n_clusters=3, random_state=0)
    df['Kluster'] = kmeans.fit_predict(X)
    # Mengubah label cluster agar dimulai dari 1
    df['Kluster'] += 1 
    
    
    
    # Visualisasi kluster
    plt.figure(figsize=(8, 6))
    plt.scatter(df['Skor Fisik'], df['Skor Verbal'], c=df['Kluster'], cmap='viridis')
    plt.xlabel('Skor Fisik')
    plt.ylabel('Skor Verbal')
    plt.title('Kluster Bullying Siswa')
    
    # Menampilkan hasil clustering
    df.rename(columns={'ID Siswa': 'ID_Siswa', 'Siswa': 'Siswa', 
                   'Skor Fisik': 'Skor_Fisik', 'Skor Verbal': 'Skor_Verbal', 
                   'Skor Psikologis': 'Skor_Psikologis'}, inplace=True)
    data_records = df.to_dict(orient='records')
    # Menyimpan gambar
    image_path = os.path.join(settings.BASE_DIR, "static/k_means.png")
    plt.savefig(image_path)
    plt.close()  # Menutup grafik setelah disimpan
    
    context = {'data_records': data_records,"title": 'Kluster Bullying Siswa',"segment": "Clustering","image_url": os.path.join(settings.STATIC_URL, 'k_means.png')}

    html_template = loader.get_template("page/peramalan.html")
    return HttpResponse(html_template.render(context, request))

@guru_bk_required
def index_guru(request):
    
    students_scores = (
        User.objects.filter(groups__name='Siswa')
        .annotate(
            skor_fisik=Sum('m_response__answer', filter=Q(m_response__kuesioner__question_type='fisik')),
            skor_verbal=Sum('m_response__answer', filter=Q(m_response__kuesioner__question_type='verbal')),
            skor_psikologis=Sum('m_response__answer', filter=Q(m_response__kuesioner__question_type='psikologis'))
        )
    )
    
    # Format data ke bentuk dictionary
    data = {
        'ID Siswa': [],
        'Siswa': [],
        'Skor Fisik': [],
        'Skor Verbal': [],
        'Skor Psikologis': []
    }

    for student in students_scores:
        data['ID Siswa'].append(student.id)
        # Gabungkan first_name dan last_name
        full_name = f"{student.first_name} {student.last_name}"
        data['Siswa'].append(full_name)
        data['Skor Fisik'].append(student.skor_fisik or 0)
        data['Skor Verbal'].append(student.skor_verbal or 0)
        data['Skor Psikologis'].append(student.skor_psikologis or 0)
    
    # Membuat DataFrame
    df = pd.DataFrame(data)
    
    # Memilih kolom yang akan digunakan untuk clustering
    X = df[['Skor Fisik', 'Skor Verbal', 'Skor Psikologis']]
    
    # Menerapkan K-Means dengan 3 kluster
    kmeans = KMeans(n_clusters=3, random_state=0)
    df['Kluster'] = kmeans.fit_predict(X)
    # Mengubah label cluster agar dimulai dari 1
    df['Kluster'] += 1 
    
    
    
    # Visualisasi kluster
    plt.figure(figsize=(8, 6))
    plt.scatter(df['Skor Fisik'], df['Skor Verbal'], c=df['Kluster'], cmap='viridis')
    plt.xlabel('Skor Fisik')
    plt.ylabel('Skor Verbal')
    plt.title('Kluster Bullying Siswa')
    
    # Menampilkan hasil clustering
    df.rename(columns={'ID Siswa': 'ID_Siswa', 'Siswa': 'Siswa', 
                   'Skor Fisik': 'Skor_Fisik', 'Skor Verbal': 'Skor_Verbal', 
                   'Skor Psikologis': 'Skor_Psikologis'}, inplace=True)
    data_records = df.to_dict(orient='records')
    # Menyimpan gambar
    image_path = os.path.join(settings.BASE_DIR, "static/k_means.png")
    plt.savefig(image_path)
    plt.close()  # Menutup grafik setelah disimpan
    
    context = {'data_records': data_records,"title": 'Kluster Bullying Siswa',"segment": "Clustering","image_url": os.path.join(settings.STATIC_URL, 'k_means.png')}

    html_template = loader.get_template("page/peramalan.html")
    return HttpResponse(html_template.render(context, request))
