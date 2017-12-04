from rest_framework import generics

from accounts.models import UserProfile

from .pagination import StandardResultsPagination
from .serializers import UserDisplaySerializer


class AccountsListAPIView(generics.ListAPIView):
    serializer_class = UserDisplaySerializer
    pagination_class = StandardResultsPagination

    def get_serializer_context(self, *args, **kwargs):
        context = super(AccountsListAPIView, self).get_serializer_context()
        context['request'] = self.request
        return context

    def get_queryset(self, *args, **kwargs):
        requested_user = self.kwargs.get("username")

        if requested_user:
            qs = UserProfile.objects.filter(user__username=requested_user)
        else:
            qs = UserProfile.objects.all()
        return qs
