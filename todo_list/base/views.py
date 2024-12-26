from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def tasklist(request):
    return HttpResponse("To do list")