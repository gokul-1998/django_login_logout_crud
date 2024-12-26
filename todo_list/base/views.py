from django.http import HttpResponse
from django.shortcuts import render
from .models import Task
from django.views.generic.list import ListView
# Create your views here.

class Tasklist(ListView):
    model = Task