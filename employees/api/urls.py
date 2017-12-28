from django.conf.urls import url

from .views import EmployeeListAPIView, EmployeeDetailAPIView

app_name = 'employee-api'
urlpatterns = [
    url(r'^$', EmployeeListAPIView.as_view(), name='list'),  # /api/employee/
    url(r'^(?P<pk>\d+)/$', EmployeeDetailAPIView.as_view(), name='detail'),
]
