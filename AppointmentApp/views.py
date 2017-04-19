# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, render_to_response, redirect
from .models import appointment
from django.shortcuts import get_object_or_404
from functools import update_wrapper

from django.contrib import admin
from django.conf.urls import url
from django.template import RequestContext



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


def appointment_detail(request, pk):
    post = get_object_or_404(appointment, pk=pk)
    return render(request, 'appointment_detail.html', {'post': post})