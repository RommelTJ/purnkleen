"""purnkleen URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include

from . import views

admin.site.site_header = "My PNK"
admin.site.site_title = "PNK Administation"
admin.site.index_title = "My PNK"

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='index'),
    url(r'^team/', include('employees.urls', namespace='employee')),
    url(r'^api/', include('accounts.api.urls', namespace='profiles-api')),
    url(r'^api/employee/', include('employees.api.urls', namespace='employee-api')),
    url(r'^', include('django.contrib.auth.urls')),
    # We edited the registrations library manually to add this change:
    # https://github.com/ubernostrum/django-registration/pull/111
    url(r'^accounts/', include('registration.backends.hmac.urls')),
    url(r'^accounts/', include('accounts.urls', namespace='profiles')),


    ####################
    # Static pages     #
    ####################
    url(r'^giveaway/$', views.giveaway, name='giveaway'),
    url(r'^about/$', views.about, name='about'),
    url(r'^vision/$', views.vision, name='vision'),
    url(r'^values/$', views.values, name='values'),
    url(r'^benefits/$', views.benefits, name='benefits'),
    url(r'^bylaws/$', views.bylaws, name='bylaws'),
    url(r'^mission-planner/$', views.mission_planner, name='mission-planner'),
    url(r'^fleet-view/$', views.fleet_view, name='fleet-view'),
    url(r'^fuel-services/$', views.fuel_services, name='fuel-services'),
    url(r'^maintenance-and-repair/$', views.maintenance_repair, name='maintenance-and-repair'),
    url(r'^transportation/$', views.transportation, name='transportation'),
    url(r'^links-and-tools/$', views.links_tools, name='links-and-tools'),
    ####################
    # End Static pages #
    ####################
]

if settings.DEBUG:
    urlpatterns += (static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
    urlpatterns += (static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
