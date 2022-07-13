from django.shortcuts import render
from django.http import HttpResponse

from .models import Question

def index(request):
    latest_question_list = Question.objects.all()
    return render(request, "polls/index.html", {
        "latest_question_list": latest_question_list
    })


def detail(request, question_id):
    return HttpResponse("Estás viendo la pregunta número {question_id}")


def results(request, question_id):
    return HttpResponse("Estás viendo los resultados de pregunta número {question_id}")


def detail(request, question_id):
    return HttpResponse("Estás votando la pregunta número {question_id}")