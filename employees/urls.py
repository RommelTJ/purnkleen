from django.conf.urls import url

from .views import (
    EmployeeCreateView,
)

app_name = 'employees'
urlpatterns = [
    url(r'^create/$', EmployeeCreateView.as_view(), name='create'),
]
