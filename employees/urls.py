from django.conf.urls import url

from .views import (
    EmployeeCreateView,
    EmployeeUpdateView,
    EmployeeDeleteView,
)

app_name = 'employees'
urlpatterns = [
    url(r'^create/$', EmployeeCreateView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/edit/$', EmployeeUpdateView.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/$', EmployeeDeleteView.as_view(), name='delete'),
]
