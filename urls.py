from django.conf.urls.defaults import patterns, include, url
import django_pdb


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'GerenciaDeRequisitos.views.home', name='home'),
    # url(r'^GerenciaDeRequisitos/', include('GerenciaDeRequisitos.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^showRevision/(\w+)/(\w+)', 'GerenciaDeRequisitos.www.views.showRevision'),
    url(r'^', include(admin.site.urls)),
)
