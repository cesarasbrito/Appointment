# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.utils import timezone

from .models import appointment

# Create your views here.

def index(request):
    today = appointment.objects.all()
    return render(request, 'index.html', {'today' : today})