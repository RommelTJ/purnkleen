from rest_framework import generics, permissions
from django.db.models import Q

from employees.models import Employee
from .pagination import StandardResultsPagination
from .serializers import EmployeeModelSerializer


class EmployeeListAPIView(generics.ListAPIView):
    serializer_class = EmployeeModelSerializer
    pagination_class = StandardResultsPagination

    def get_serializer_context(self, *args, **kwargs):
        context = super(EmployeeListAPIView, self).get_serializer_context(*args, **kwargs)
        context['request'] = self.request
        return context

    def get_queryset(self, *args, **kwargs):
        qs = Employee.objects.exclude(type__in=["RET", "KIA"])

        query = self.request.GET.get("q", None)
        if query is not None:
            type_search = query
            activity_search = query
            if query is not "":
                type_search = self.search(Employee.EMPLOYEE_DICT, query)
                activity_search = self.search(Employee.ACTIVITY_DICT, query)

            if type_search is not "":
                qs = qs.filter(type__icontains=type_search)
            elif activity_search is not "":
                qs = qs.filter(
                    Q(primary_activity__icontains=activity_search) |
                    Q(secondary_activity__icontains=activity_search)
                )
            else:
                qs = qs.filter(
                    Q(user__last_name__icontains=query) |
                    Q(user__first_name__icontains=query) |
                    Q(callsign__icontains=query)
                )
        return qs

    def search(self, values, searchFor):
        # This search is not very efficient. We should replace it.
        for k in values:
            if searchFor.lower() in values[k].lower():
                return k
        return ""


class EmployeeDetailAPIView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeModelSerializer
    pagination_class = StandardResultsPagination
    permission_classes = [permissions.AllowAny]

    def get_queryset(self, *args, **kwargs):
        emp_no = self.kwargs.get("pk")
        return Employee.objects.filter(emp_no=emp_no)
