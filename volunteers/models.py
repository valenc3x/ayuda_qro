# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Institution(models.Model):
    name = models.CharField('Nombre', max_length=140)
    description = models.TextField('Descripción')
    address = models.TextField('Dirección')
    telephone = models.CharField('Teléfono', max_length=15, null=True,
                                 blank=True)
    email = models.EmailField('Correo Electrónico', null=True, blank=True)
    web_address = models.URLField('Dirección Web', null=True, blank=True)
    administrator = models.ForeignKey(User, related_name='institutions',
                                      verbose_name='Encargado')

    def __unicode__(self):
        return self.name

    def get_details(self):
        return {
            'id': self.id,
            'data': (
                ('Nombre', self.name),
                ('Descripción', self.description),
                ('Dirección', self.address),
                ('Teléfono', self.telephone),
                ('Correo Electrónico', self.email),
                ('Dirección Web', self.web_address)
            )
        }

    class Meta():
        verbose_name = 'Institución'


class Program(models.Model):
    name = models.CharField('Nombre',max_length=140)
    description = models.TextField('Descripción')
    requirements = models.TextField('Conocimientos necesarios', null=True,
                                    blank=True)
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
    institution = models.ForeignKey(Institution, related_name='programs',
                                    verbose_name='Institucion')

    def __unicode__(self):
        return '%s - %s'  % (self.name, self.institution.name)

    @classmethod
    def get_by_id(p_id):
        return Program.objects.get(id=p_id)

    @classmethod
    def get_by_name(p_name):
        return Program.objects.get(name=p_name)

    @classmethod
    def get_by_institution(i_id):
        return Program.objects.get()

    def get_details(self):
        return {
            'id': self.id,
            'data': (
                ('Nombre', self.name),
                ('Descripción', self.description),
                ('Conocimientos necesarios', self.requirements),
                ('Periodo de tiempo', self.get_period_display()),
                ('Horario', self.get_time_of_day_display()),
            )
        }

    class Meta():
        verbose_name = 'Proyecto'

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
    occupation = models.CharField('Ocupación',max_length=140, null=True,
                                  blank=True)
    email = models.EmailField('Correo Electrónico', null=True, blank=True)
    telephone = models.CharField("Teléfono", max_length=15)
    project = models.ForeignKey(Program, related_name='volunteers',
                                verbose_name='Programa')
    skills = models.TextField('Habilidades', null=True, blank=True)
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

    def get_details(self):
        return {
            'id': self.id,
            'data': (
                ('Nombre', self.full_name),
                ('Fecha de nacimiento', self.birth_date),
                ('Sexo', self.get_gender_display()),
                ('Programa', self.project),
                ('Horario Disponible', self.get_time_availability_display()),
                ('Teléfono', self.telephone),
                ('Correo Electrónico', self.email),
                ('Ocupación', self.occupation),

            )
        }

    class Meta():
        verbose_name = 'Voluntario'

