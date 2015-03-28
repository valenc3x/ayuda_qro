# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Institution(models.Model):
    name = models.CharField('Nombre', max_length=140)
    description = models.TextField('Descripción')
    address = models.TextField('Dirección')
    telephone = models.CharField("Teléfono", max_length=15)
    email = models.EmailField()
    web_address = models.URLField('Dirección Web')
    administrator = models.OneToOneField(User, related_name='institution')


class Program(models.Model):
    name = models.CharField('Nombre',max_length=140)
    description = models.TextField('Descripción')
    requirements = models.TextField('Conocimientos necesarios')
    PERIOD = (
        (101, 'Diario'),
        (102, 'Semanal'),
        (103, 'Por Temporada')
    )
    period = models.IntegerField('Periodo de tiempo', choices=PERIOD)
    TIME = (
        (201, 'Mañana'),
        (202, 'Tarde'),
        (203, 'Noche'),
        (204, 'Medio día'),
        (205, 'Todo el día')
    )
    time_of_day = models.IntegerField('Horario', choices=TIME)


class VolunteerRegistry(models.Model):
    name = models.CharField('Nombre', max_length=140)
    father_last_name =  models.CharField('Apellido Paterno', max_length=140)
    mother_last_name = models.CharField('Apellido Materno', max_length=140)
    telephone = models.CharField("Teléfono", max_length=15)
    email = models.EmailField()
    project = models.ForeignKey(Program,related_name='volunteers')
