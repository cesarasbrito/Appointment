# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import codecs

from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.forms import forms
from django.urls import reverse
from django.core import urlresolvers
from django.contrib.contenttypes.models import ContentType

from AppointmentApp.choices import *
from django.contrib import admin




# class AdminURLMixin(object):
#     def get_admin_url(self):
#         content_type = ContentType.objects.get_for_model(self.__class__)
#         return reverse("admin:%s_%s_change" % (
#             content_type.app_label,
#             content_type.model),
#             args=(self.id,))



# Create your models here.
class user(models.Model):
    name = models.TextField(max_length=150)
    email = models.TextField(max_length=50)
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name = "Usuario"



class patient(models.Model):
    name = models.TextField(max_length=150)
    email = models.TextField(max_length=50)
    phone = models.TextField(max_length=30)
    cel = models.TextField(max_length=30)
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name = "Paciente"



class daysOfWeek(models.Model):
    name = models.TextField()
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name = "Dias da Semana"


class attendance(models.Model):
    name = models.TextField(max_length=30)
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name = "Tipo de Atendimento"




class appointment(models.Model):
    user = models.ForeignKey(user)
    patient = models.ForeignKey(patient)
    #day = models.ForeignKey(daysOfWeek)
    #hour = models.TimeField()
    date = models.DateTimeField()
    attendance = models.ForeignKey(attendance)
    obs = models.TextField(max_length=300, default='')
    status = models.TextField(choices=STATUS_ATTENDENCE, default=1)

    def get_admin_url(self):
        content_type = ContentType.objects.get_for_model(self.__class__)
        return urlresolvers.reverse("admin:%s_%s_change" % (content_type.app_label, content_type.model),
                                    args=(self.id,))
    def __unicode__(self):
        return self.user.name
    class Meta:
        verbose_name = "Agendamento"









