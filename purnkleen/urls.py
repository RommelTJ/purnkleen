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

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^$', views.home, name='index'),
    url(r'^giveaway/$', views.giveaway, name='giveaway'),

    #########################
    # Start About Views     #
    #########################
    url(r'^about/$', views.about, name='about'),
    url(r'^vision/$', views.vision, name='vision'),
    url(r'^values/$', views.values, name='values'),
    # url(r'^team/$', views.ProfileListView.as_view(), name='team'),
    url(r'^benefits/$', views.benefits, name='benefits'),
    url(r'^bylaws/$', views.bylaws, name='bylaws'),
    url(r'^join/$', views.join, name='join'),
    # url(r'^employees/profile/create/$', views.PNKProfileCreateView.as_view(), name='pnk_profile_create'),
    #########################
    # End About Views       #
    #########################

    #########################
    # Start Solutions Views #
    #########################
    url(r'^mission-planner/$', views.mission_planner, name='mission-planner'),
    url(r'^fleet-view/$', views.fleet_view, name='fleet-view'),
    #########################
    # End Solutions Views   #
    #########################

    #########################
    # Start Services Views  #
    #########################
    url(r'^fuel-services/$', views.fuel_services, name='fuel-services'),
    url(r'^maintenance-and-repair/$', views.maintenance_repair, name='maintenance-and-repair'),
    url(r'^transportation/$', views.transportation, name='transportation'),
    #########################
    # End Services Views    #
    #########################

    #########################
    # Start Knowledge Views #
    #########################
    url(r'^links-and-tools/$', views.links_tools, name='links-and-tools'),
    #########################
    # End Knowledge Views   #
    #########################
]

if settings.DEBUG:
    urlpatterns += (static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
