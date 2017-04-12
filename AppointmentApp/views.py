# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.utils import timezone

from django.utils.safestring import mark_safe

from .models import appointment, CalendarEvent
from datetime import date, datetime

from calendar import HTMLCalendar, calendar
from django.views.generic import ListView, TemplateView

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