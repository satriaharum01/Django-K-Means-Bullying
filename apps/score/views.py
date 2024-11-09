from django.db.models import Sum, Q, Count
from django.shortcuts import redirect
from django.contrib import messages
from django.template import loader
from django.http import HttpResponse, JsonResponse

# Decorators
from ..decorators import admin_required, guru_bk_required

# Models Import
from django.contrib.auth.models import User
from ..models import m_kuesioner, m_response

# Create your views here.


@admin_required
def index(request):
    title = "Data Hasil Kuesioner"
    page = "Score"
    context = {"page": page, "title": title}

    html_template = loader.get_template("page/score.html")
    return HttpResponse(html_template.render(context, request))

@guru_bk_required
def index_guru(request):
    title = "Data Hasil Kuesioner"
    page = "Score"
    context = {"page": page, "title": title}

    html_template = loader.get_template("page/score.html")
    return HttpResponse(html_template.render(context, request))


# JSON DATA OBJECT
def json(request):

    if request.method == "GET":
        students_scores = User.objects.filter(groups__name="Siswa").annotate(
            skor_fisik=Sum(
                "m_response__answer",
                filter=Q(m_response__kuesioner__question_type="fisik"),
            ),
            skor_verbal=Sum(
                "m_response__answer",
                filter=Q(m_response__kuesioner__question_type="verbal"),
            ),
            skor_psikologis=Sum(
                "m_response__answer",
                filter=Q(m_response__kuesioner__question_type="psikologis"),
            ),
            jawaban=Count("m_response__answer")
        )
        # Format data ke bentuk dictionary
        
        kuesioner = m_kuesioner.objects.count()
        data = []
        i = 1
        for student in students_scores:
            DT_RowIndex=i
            full_name = f"{student.first_name} {student.last_name}"
            answer = f"{student.jawaban} / {kuesioner}"
            data.append({
                "DT_RowIndex":DT_RowIndex,
                "ID_Siswa":student.id,
                "Siswa":full_name,
                "jawaban": answer,
                "Skor_Fisik":(student.skor_fisik or 0),
                "Skor_Verbal":(student.skor_verbal or 0),
                "Skor_Psikologis":(student.skor_psikologis or 0),
            })
            i= i+1
            
        data = {"data": data}
        return JsonResponse(data, safe=False)
    else:
        messages.success(request, "Invalid Method")
        return redirect("score")


# FIND DATA OBJECT
def find(request, data_id):
    auth_id = request.user.id
    if request.method == "GET":
        all_objs = m_kuesioner.objects.all().values("id").filter(id=data_id)
        for load in all_objs:
            kuesioner = m_kuesioner.objects.get(id=load["id"])
            response = m_response.objects.filter(
                user_id=auth_id, kuesioner=kuesioner
            ).first()
            load["kuesioner"] = load["id"]
            if not response:
                load["answer"] = 0
            else:
                load["answer"] = response.answer
        data = {"data": list(all_objs)}
        return JsonResponse(data, safe=False)
    else:
        messages.success(request, "Invalid Method")
        return redirect("kuesioner")
