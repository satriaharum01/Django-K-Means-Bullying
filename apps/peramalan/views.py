import os
from django import template
from django.core import serializers
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

# Tools
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Models Import
from ..models import m_data

month = ['','Januari','Febuari','Maret','April','Mei','Juni','Juli','Agustus','September','Oktober','November','Desember']

# Create your views here.


@login_required(login_url="/login/")
def index(request):
    # Mengambil semua data historis dari database
    data = m_data.objects.all()

    # Mengambil data ekspor dan permintaan
    x = np.array([d.ekspor for d in data]).reshape(-1, 1)
    y = np.array([d.jumlah for d in data])
    z = []
    
    all_objs = np.array([d.periode for d in data])
    for load in all_objs:
        periode = load
        bulan = int(periode[5:7])
        load = month[bulan] +' '+ load[0:4]
        z.append(load)
    
    # Membuat model regresi linear
    model = LinearRegression()

    # Melatih model
    model.fit(x, y)

    # Melakukan prediksi
    # Prediksi menggunakan data yang sama
    y_pred = model.predict(x)

    # Menghitung residual (nilai aktual - nilai prediksi)
    residuals = y - y_pred


    # Evaluasi model
    mse = mean_squared_error(y, y_pred)
    r2 = r2_score(y, y_pred)
    # Menghitung residual (nilai aktual - nilai prediksi)
    residuals = y - y_pred

    # Membuat dataframe untuk membandingkan nilai aktual, prediksi, dan residual
    comparison_df = pd.DataFrame({
        'Ekspor': x.ravel(),
    })
    
    residual_data = zip(z,y,y_pred,residuals)
    #print(comparison_df.head())
    
    # Melihat koefisien regresi dan intercept
    #print("Koefisien (Slope):", model.coef_[0])
    #print("Intercept:", model.intercept_)
    #print(f"Mean Squared Error: {mse}")
    #print(f"R-squared: {r2}")
    #print(f"Prediksi Bulan Depan: {y_pred}")

    context = {"title": 'Peramalan Regresi Linear',"segment": "peramalan", "slope":model.coef_[0],"intercept":model.intercept_,"prediksi": y_pred[0], "mse": mse, "r2": r2, "data": residual_data, "actual_data":data}

    html_template = loader.get_template("page/peramalan.html")
    return HttpResponse(html_template.render(context, request))
