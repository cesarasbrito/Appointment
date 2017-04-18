# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, render_to_response, redirect
from .models import appointment, MyForm
from django.shortcuts import get_object_or_404



# Create your views here.

def index(request):
    today = appointment.objects.all()
    return render(request, 'index.html', {'today' : today})



def home(request):
    today = appointment.objects.all()
    return render(request, 'index.html', {'today' : today})

def calendar(request):
    today = appointment.objects.all()
    return render(request, 'calendar.html', {'today' : today})

