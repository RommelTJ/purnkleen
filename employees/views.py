from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .forms import EmployeeForm
from .models import Employee, generate_next_emp_no


class EmployeeCreateView(LoginRequiredMixin, CreateView):
    form_class = EmployeeForm
    template_name = 'employees/employee_create.html'
    success_url = reverse_lazy('index')

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        if context.get('employee') is None:
            form = EmployeeForm()
            return render(request, self.get_template_name(), {'form': form})
        return HttpResponseRedirect('/')

    def post(self, request, *args, **kwargs):
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            self.object = form.save(commit=False)
            self.object.emp_no = generate_next_emp_no()
            self.object.user = self.request.user
            self.object.type = 'AFF'
            self.object.save()
            return HttpResponseRedirect('/')
        return render(request, self.template_name, {'form': form})

    def get_template_name(self):
        return self.template_name

    def get_context_data(self):
        return {
            'employee': self.get_employee(),
        }

    def get_employee(self):
        qs = Employee.objects.filter(
            user__exact=self.request.user
        ).filter(
            type__in=["MEM","AFF"]
        ).first()
        return qs