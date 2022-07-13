from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Página principal página Platzi App")


def detail(request, question_id):
    return HttpResponse("Estás viendo la pregunta número {question_id}")


def results(request, question_id):
    return HttpResponse("Estás viendo los resultados de pregunta número {question_id}")


def detail(request, question_id):
    return HttpResponse("Estás votando la pregunta número {question_id}")