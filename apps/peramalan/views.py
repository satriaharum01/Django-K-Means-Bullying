import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, Http404
from django.conf import settings


# Create your views here.


@login_required(login_url="/login/")
def index(request):
    
    # Membuat data dummy
    data = {
        'ID Siswa': [1, 2, 3, 4, 5],
        'Skor Fisik': [30, 20, 35, 15, 25],
        'Skor Verbal': [28, 22, 30, 20, 18],
        'Skor Psikologis': [25, 15, 28, 10, 20]
    }
    
    # Membuat DataFrame
    df = pd.DataFrame(data)
    
    # Memilih kolom yang akan digunakan untuk clustering
    X = df[['Skor Fisik', 'Skor Verbal', 'Skor Psikologis']]
    
    # Menerapkan K-Means dengan 3 kluster
    kmeans = KMeans(n_clusters=3, random_state=0)
    df['Kluster'] = kmeans.fit_predict(X)
    
    # Menampilkan hasil clustering
    print(df)
    
    # Visualisasi kluster
    plt.figure(figsize=(8, 6))
    plt.scatter(df['Skor Fisik'], df['Skor Verbal'], c=df['Kluster'], cmap='viridis')
    plt.xlabel('Skor Fisik')
    plt.ylabel('Skor Verbal')
    plt.title('Kluster Bullying Siswa')

    # Menyimpan gambar
    image_path = os.path.join(settings.MEDIA_ROOT, 'k_means.png')
    plt.savefig(image_path)
    plt.close()  # Menutup grafik setelah disimpan
    
    context = {"title": 'Peramalan Regresi Linear',"segment": "peramalan","image_url": os.path.join(settings.STATIC_URL, 'k_means.png')}

    html_template = loader.get_template("page/peramalan.html")
    return HttpResponse(html_template.render(context, request))
