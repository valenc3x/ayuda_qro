from django.conf.urls import patterns, include, url
from django.contrib import admin
from volunteers.views import InstitutionCreate, InstitutionUpdate, \
    InstitutionDelete, InstitutionList, InstitutionView
from volunteers.views import ProgramCreate, ProgramUpdate, \
    ProgramDelete, ProgramList, ProgramView
from volunteers.views import VolunteerRegistryCreate, VolunteerRegistryUpdate, \
    VolunteerRegistryDelete, VolunteerRegistryList, VolunteerRegistryView


urlpatterns = patterns('volunteers.views',
    #
    # Simple url
    #
    url(r'^$', 'home', name='home'),
    #
    # Institutions
    #
    url(
        r'^instituciones/nueva$',
        InstitutionCreate.as_view(),
        name='create_institution'
    ),
    url(
        r'^instituciones/editar/(?P<pk>\d+)$',
        InstitutionUpdate.as_view(),
        name='update_institution'
    ),
    url(
        r'^instituciones/eliminar/(?P<pk>\d+)$',
        InstitutionDelete.as_view(),
        name='delete_institution'
    ),
    url(
        r'^instituciones/(?P<pk>\d+)$',
        InstitutionView.as_view(),
        name='detail_institution'
    ),
    url(
        r'^instituciones/$',
        InstitutionList.as_view(),
        name='list_institution'
    ),
    #
    # Programs
    #
    url(
        r'^programas/nueva$',
        ProgramCreate.as_view(success_url='/programas'),
        name='create_program'
    ),
    url(
        r'^programas/editar/(?P<pk>\d+)$',
        ProgramUpdate.as_view(),
        name='update_program'
    ),
    url(
        r'^programas/eliminar/(?P<pk>\d+)$',
        ProgramDelete.as_view(),
        name='delete_program'
    ),
    url(
        r'^programas/(?P<pk>\d+)$',
        ProgramView.as_view(),
        name='detail_program'
    ),
    url(
        r'^programas/$',
        ProgramList.as_view(),
        name='list_program'
    ),
    #
    # Volunteer
    #
    url(
        r'^voluntarios/nuevo$',
        VolunteerRegistryCreate.as_view(success_url='/voluntarios'),
        name='create_volunteer'
    ),
    url(
        r'^voluntarios/editar/(?P<pk>\d+)$',
        VolunteerRegistryUpdate.as_view(),
        name='update_volunteer'
    ),
    url(
        r'^voluntarios/eliminar/(?P<pk>\d+)$',
        VolunteerRegistryDelete.as_view(),
        name='delete_volunteer'
    ),
    url(
        r'^voluntarios/(?P<pk>\d+)$',
        VolunteerRegistryView.as_view(),
        name='detail_volunteer'
    ),
    url(
        r'^voluntarios/$',
        VolunteerRegistryList.as_view(),
        name='list_volunteer'
    ),

    url(r'^admin/', include(admin.site.urls)),
)
