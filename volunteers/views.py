from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Institution, Program, VolunteerRegistry

# Create your views here.

def home(request):
    return render(request)

class InstitutionCreate(CreateView):
    model = Institution
    fields = [
        'name',
        'description',
        'address',
        'telephone',
        'email',
        'web_address'
    ]


class InstitutionUpdate(UpdateView):
    model = Institution
    fields = [
        'name',
        'description',
        'address',
        'telephone',
        'email',
        'web_address'
    ]


class InstitutionDelete(DeleteView):
    model = Institution
    success_url = reverse_lazy('author-list')


class ProgramCreate(CreateView):
    model = Program
    fields = [
        'name',
        'description',
        'period',
        'time_of_day',
        'description'
    ]


class ProgramUpdate(UpdateView):
    model = Program
    fields = [
        'name',
        'description',
        'period',
        'time_of_day',
        'description'
    ]


class ProgramDelete(DeleteView):
    model = Program
    success_url = reverse_lazy('author-list')


class VolunteerRegistryCreate(CreateView):
    model = VolunteerRegistry
    fields = [
        'name',
        'father_last_name',
        'mother_last_name',
        'telephone',
        'email',
        'project'
    ]


class VolunteerRegistryDelete(DeleteView):
    model = VolunteerRegistry
    success_url = reverse_lazy('author-list')
