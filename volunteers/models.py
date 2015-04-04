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
    administrator = models.OneToOneField(User, related_name='institutions')

    def __unicode__(self):
        return self.name


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
    institution = models.ForeignKey(Institution, related_name='programs')

    def __unicode__(self):
        return '%s de %s'  % (self.name, self.insitution.name)

    @classmethod
    def get_by_id(p_id):
        return Program.objects.get(id=p_id)

    @classmethod
    def get_by_name(p_name):
        return Program.objects.get(name=p_name)

    @classmethod
    def get_by_institution(i_id):
        return Program.objects.get()

class VolunteerRegistry(models.Model):
    name = models.CharField('Nombre', max_length=140)
    father_last_name =  models.CharField('Apellido Paterno', max_length=140)
    mother_last_name = models.CharField('Apellido Materno', max_length=140)
    birth_date = models.DateField('Fecha de nacimiento')
    GENDER = (
        (301, 'Hombre'),
        (302, 'Mujer')
    )
    gender = models.IntegerField('Sexo', choices=GENDER)
    occupation = models.CharField('Ocupación',max_length=140)
    email = models.EmailField('Correo Electronico')
    telephone = models.CharField("Teléfono", max_length=15)
    project = models.ForeignKey(Program, related_name='volunteers')
    skills = models.TextField('Habilidades')
    TIME = (
        (201, 'Mañana'),
        (202, 'Tarde'),
        (203, 'Noche'),
        (204, 'Medio día'),
        (205, 'Todo el día')
    )
    time_availability = models.IntegerField('Horario Disponible', choices=TIME)

    def _get_full_name(self):
        return '%s %s %s' % \
               (self.name, self.father_last_name, self.mother_last_name)

    full_name = property(_get_full_name)

    def __unicode__(self):
        return '%s a %s' % (self.name, self.project.name)

