from django.conf.urls import url

from .views import AccountsListAPIView

app_name = 'accounts-api'
urlpatterns = [
    url(r'^$', AccountsListAPIView.as_view(), name='list'),  # /api/
]
