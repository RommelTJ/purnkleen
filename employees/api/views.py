from rest_framework import generics, permissions

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
        qs = Employee.objects.filter(type__in=["MEM", "AFF", "PRE", "SEC", "CFO"])
        return qs


class EmployeeDetailAPIView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeModelSerializer
    pagination_class = StandardResultsPagination
    permission_classes = [permissions.AllowAny]

    def get_queryset(self, *args, **kwargs):
        emp_no = self.kwargs.get("pk")
        return Employee.objects.filter(emp_no=emp_no)
