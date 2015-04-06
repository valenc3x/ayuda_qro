from django.conf.urls import patterns, include, url
from django.contrib import admin
from volunteers.views import InstitutionCreate, InstitutionUpdate, InstitutionDelete, InstitutionList, InstitutionView
from volunteers.views import ProgramCreate, ProgramUpdate, ProgramDelete
from volunteers.views import VolunteerRegistryCreate, VolunteerRegistryUpdate, VolunteerRegistryDelete


urlpatterns = patterns('volunteers.views',
    # Examples:
    url(r'^$', 'home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(
        r'^instituciones/nueva$',
        InstitutionCreate.as_view(success_url='/'),
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
    url(r'^admin/', include(admin.site.urls)),
)
