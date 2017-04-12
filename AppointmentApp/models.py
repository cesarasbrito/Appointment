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




class CalendarEvent(models.Model):
    """
    Calendar Events
    """
    CSS_CLASS_CHOICES = (
        ('', ('Normal')),
        ('event-warning',  ('Warning')),
        ('event-info',  ('Info')),
        ('event-success',  ('Success')),
        ('event-inverse',  ('Inverse')),
        ('event-special',  ('Special')),
        ('event-important',  ('Important')),
    )
    title = models.CharField(max_length=255, verbose_name= ('Title'))
    url = models.URLField(verbose_name= ('URL'), null=True, blank=True)
    css_class = models.CharField(blank=True, max_length=20, verbose_name= ('CSS Class'),
                                 choices=CSS_CLASS_CHOICES)
    start = models.DateTimeField(verbose_name= ('Start Date'))
    end = models.DateTimeField(verbose_name= ('End Date'), null=True,
                               blank=True)

    @property
    def start_timestamp(self):
        """
        Return start date as timestamp
        """
        return datetime_to_timestamp(self.start)

    @property
    def end_timestamp(self):
        """
        Return end date as timestamp
        """
        return datetime_to_timestamp(self.end)

    def __unicode__(self):
        return self.title
