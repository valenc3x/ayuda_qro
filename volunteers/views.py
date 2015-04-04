from django.shortcuts import render_to_response
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Institution, Program, VolunteerRegistry

# Create your views here.

def home(request):
    return render_to_response('home.html')

class InstitutionCreate(CreateView):
    template_name = 'form.html'
    model = Institution


class InstitutionUpdate(UpdateView):
    template_name = 'form.html'
    model = Institution


class InstitutionDelete(DeleteView):
    template_name = 'form.html'
    model = Institution
    success_url = reverse_lazy('author-list')


class ProgramCreate(CreateView):
    template_name = 'form.html'
    model = Program



class ProgramUpdate(UpdateView):
    template_name = 'form.html'
    model = Program



class ProgramDelete(DeleteView):
    template_name = 'form.html'
    model = Program
    success_url = reverse_lazy('author-list')


class VolunteerRegistryCreate(CreateView):
    template_name = 'form.html'
    model = VolunteerRegistry


class VolunteerRegistryDelete(DeleteView):
    template_name = 'form.html'
    model = VolunteerRegistry
    success_url = reverse_lazy('author-list')
