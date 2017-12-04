from django.conf.urls import url

from .views import UserDetailView

app_name = 'profiles'
urlpatterns = [
    url(r'^(?P<username>[\w.@+-]+)/$', UserDetailView.as_view(), name='detail'), # /tweet/1/
]