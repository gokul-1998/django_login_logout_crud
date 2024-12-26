from django.http import HttpResponse
from django.shortcuts import render
from .models import Task
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
# Create your views here.

class Tasklist(ListView):
    model = Task
    context_object_name = 'tasks'

class  TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/task.html'
