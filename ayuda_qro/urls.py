from django.conf.urls import patterns, include, url
from django.contrib import admin
from volunteers.views import *

urlpatterns = patterns('volunteers.views',
    # Examples:
    url(r'^$', 'home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(
        r'^instituciones/nueva$',
        InstitutionCreate.as_view(),
        name='create_institution'
    ),
    url(
        r'^institiciones/editar/(?P<id>\d+)',
        InstitutionUpdate.as_view(),
        name='update_institution'
    ),
    url(r'^admin/', include(admin.site.urls)),
)
