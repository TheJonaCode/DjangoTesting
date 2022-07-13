from django.shortcuts import render
from django.http import HttResponse

# Create your views here.
def index(request):
    return HttResponse("Hello World")