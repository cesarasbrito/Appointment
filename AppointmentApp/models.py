# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import codecs
from django.db import models
from django.utils.encoding import smart_unicode


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
    def __unicode__(self):
        return self.user.name
    class Meta:
        verbose_name = "Agendamento"



