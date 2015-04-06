# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.core.urlresolvers import reverse_lazy
from .models import Institution, Program, VolunteerRegistry

# Create your views here.

def home(request):
    return render_to_response('home.html')


#
# Institutions
#

class InstitutionCreate(CreateView):
    template_name = 'form.html'
    model = Institution


class InstitutionUpdate(UpdateView):
    template_name = 'form.html'
    model = Institution


class InstitutionDelete(DeleteView):
    template_name = 'confirm.html'
    model = Institution
    success_url = reverse_lazy('list_institution')


class InstitutionView(DetailView):
    template_name = 'detail.html'
    model = Institution
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
    template_name = 'form.html'
    model = Program



class ProgramUpdate(UpdateView):
    template_name = 'form.html'
    model = Program



class ProgramDelete(DeleteView):
    template_name = 'form.html'
    model = Program
    success_url = reverse_lazy('home')


class VolunteerRegistryCreate(CreateView):
    template_name = 'form.html'
    model = VolunteerRegistry


class VolunteerRegistryUpdate(UpdateView):
    template_name = 'form.html'
    model = VolunteerRegistry


class VolunteerRegistryDelete(DeleteView):
    template_name = 'form.html'
    model = VolunteerRegistry
    success_url = reverse_lazy('home')
