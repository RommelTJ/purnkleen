from django.conf.urls import url

from .views import (
    EmployeeCreateView,
    EmployeeUpdateView,
)

app_name = 'employees'
urlpatterns = [
    url(r'^create/$', EmployeeCreateView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/edit/$', EmployeeUpdateView.as_view(), name='update'),
]
