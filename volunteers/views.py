# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.core.urlresolvers import reverse_lazy
from .models import Institution, Program, VolunteerRegistry

#
# Create your views here
#

def home(request):
    return render_to_response('home.html')


#
# Institutions
#

class InstitutionCreate(CreateView):
    model = Institution
    template_name = 'form.html'
    title = 'Nueva Institiución'
    success_url = '/instituciones'


class InstitutionUpdate(UpdateView):
    model = Institution
    template_name = 'form.html'
    title = 'Editar Institución'
    success_url = '/instituciones'

class InstitutionDelete(DeleteView):
    template_name = 'confirm.html'
    model = Institution
    success_url = reverse_lazy('list_institution')


class InstitutionView(DetailView):
    model = Institution
    template_name = 'detail.html'
    title = 'Detalles de la Institución'


    def get_object(self):
        object = super(InstitutionView, self).get_object()
        return object.get_details()


class InstitutionList(ListView):
    model = Institution
    template_name = 'list.html'
    title = "Instituciones"

#
# Programs
#

class ProgramCreate(CreateView):
    model = Program
    template_name = 'form.html'
    title = 'Nuevo Programa'
    success_url = '/programas'


class ProgramUpdate(UpdateView):
    model = Program
    template_name = 'form.html'
    title = 'Editar Programa'
    success_url = '/programas'


class ProgramDelete(DeleteView):
    model = Program
    template_name = 'confirm.html'
    success_url = reverse_lazy('list_program')


class ProgramView(DetailView):
    model = Program
    template_name = 'detail.html'
    title = 'Detalles del Programa'

    def get_object(self):
        object = super(ProgramView, self).get_object()
        return object.get_details()


class ProgramList(ListView):
    model = Program
    template_name = 'list.html'
    title = "Programas"

#
# Volunteers
#

class VolunteerRegistryCreate(CreateView):
    model = VolunteerRegistry
    template_name = 'form.html'
    title = 'Registro de Voluntario'
    success_url = '/voluntarios'


class VolunteerRegistryUpdate(UpdateView):
    model = VolunteerRegistry
    template_name = 'form.html'
    title = 'Editar Registro de Voluntario'
    success_url = '/voluntarios'


class VolunteerRegistryDelete(DeleteView):
    model = VolunteerRegistry
    template_name = 'confirm.html'
    success_url = reverse_lazy('list_volunteer')


class VolunteerRegistryView(DetailView):
    model = VolunteerRegistry
    template_name = 'detail.html'
    title = 'Detalles del Voluntario'

    def get_object(self):
        object = super(VolunteerRegistryView, self).get_object()
        return object.get_details()


class VolunteerRegistryList(ListView):
    model = VolunteerRegistry
    template_name = 'list.html'
    title = "Voluntarios"

