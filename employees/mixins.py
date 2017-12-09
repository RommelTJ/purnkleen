from django.http import HttpResponseRedirect


class UserOwnerMixin(object):

    def get_queryset(self):
        qs = super(UserOwnerMixin, self).get_queryset()
        return qs.filter(user__exact=self.request.user)

    def dispatch(self, request, *args, **kwargs):
        if self.get_queryset().count() == 0:
            return HttpResponseRedirect('/')
        return super(UserOwnerMixin, self).dispatch(request, *args, **kwargs)
