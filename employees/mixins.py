from django.http import HttpResponseRedirect
from django.urls import reverse_lazy


class UserOwnerMixin(object):

    def get_queryset(self):
        qs = super(UserOwnerMixin, self).get_queryset()
        qs = qs.filter(
            user__exact=self.request.user
        ).filter(
            type__in=["MEM","AFF"]
        )
        return qs

    def dispatch(self, request, *args, **kwargs):
        # Only dispatch if we are the owner of the user object.
        # Employees can only have one active profile at a time.
        if self.get_queryset().count == 1:
            employee = self.get_queryset().first()
            if employee.emp_no == kwargs['pk']:
                return super(UserOwnerMixin, self).dispatch(request, *args, **kwargs)
            else:
                return HttpResponseRedirect(reverse_lazy('employee:list'))
        else:
            return HttpResponseRedirect(reverse_lazy('employee:list'))
