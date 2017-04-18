# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.admin import AdminSite

from .models import user,appointment,attendance,patient,daysOfWeek

from django.contrib import admin



# Register your models here.
admin.site.register(user)
admin.site.register(appointment)
admin.site.register(attendance)
admin.site.register(patient)
admin.site.register(daysOfWeek)


