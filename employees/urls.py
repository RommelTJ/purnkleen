from django.conf.urls import url

from .views import (
    EmployeeListView,
    EmployeeCreateView,
    EmployeeUpdateView,
    EmployeeDeleteView,
    EmployeeDetailView,
)

app_name = 'employees'
urlpatterns = [
    url(r'^$', EmployeeListView.as_view(), name='list'),
    url(r'^create/$', EmployeeCreateView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/edit/$', EmployeeUpdateView.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/$', EmployeeDeleteView.as_view(), name='delete'),
    url(r'^(?P<pk>\d+)/$', EmployeeDetailView.as_view(), name='detail'),
]
