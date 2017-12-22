from django.conf.urls import url

from .views import (
    EmployeeListView,
    EmployeeCreateView,
    EmployeeUpdateView,
    EmployeeDetailView,
    employee_retire_view,
    employee_kia_view,
)

app_name = 'employees'
urlpatterns = [
    url(r'^$', EmployeeListView.as_view(), name='list'),
    url(r'^create/$', EmployeeCreateView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/edit/$', EmployeeUpdateView.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/$', EmployeeDetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/retire/$', employee_retire_view, name='retire'),
    url(r'^(?P<pk>\d+)/kia/$', employee_kia_view, name='kia'),
]
