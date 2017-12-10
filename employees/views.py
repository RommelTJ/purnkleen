from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from .forms import EmployeeForm
from .mixins import UserOwnerMixin
from .models import Employee, generate_next_emp_no


class EmployeeCreateView(LoginRequiredMixin, CreateView):
    form_class = EmployeeForm
    template_name = 'employees/employee_create.html'
    success_url = reverse_lazy('index')

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        if context.get('employee') is None:
            initial = self.get_initial()
            initial['first_name'] = self.request.user.first_name
            initial['last_name'] = self.request.user.last_name
            form = EmployeeForm(initial=initial)
            return render(request, self.template_name, {'form': form})
        return HttpResponseRedirect('/')

    def post(self, request, *args, **kwargs):
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            self.object = form.save(commit=False)
            self.object.emp_no = generate_next_emp_no()
            self.object.user = self.request.user
            self.object.user.first_name = form.data['first_name']
            self.object.user.last_name = form.data['last_name']
            self.object.user.save()
            self.object.type = 'AFF'
            self.object.save()
            return HttpResponseRedirect('/')
        return render(request, self.template_name, {'form': form})

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


class EmployeeUpdateView(LoginRequiredMixin, UserOwnerMixin, UpdateView):
    form_class = EmployeeForm
    template_name = 'employees/employee_update.html'
    model = Employee
    success_url = reverse_lazy('index')

    def get_initial(self):
        initial = super(EmployeeUpdateView, self).get_initial()
        initial['first_name'] = self.request.user.first_name
        initial['last_name'] = self.request.user.last_name
        return initial

    def post(self, request, *args, **kwargs):
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            self.object = form.save(commit=False)
            self.object.emp_no = kwargs['pk']
            self.object.user = self.request.user
            self.object.user.first_name = form.data['first_name']
            self.object.user.last_name = form.data['last_name']
            self.object.user.save()
            self.object.save()
            return HttpResponseRedirect('/')
        return render(request, self.template_name, {'form': form})


class EmployeeDeleteView(LoginRequiredMixin, UserOwnerMixin, DeleteView):
    model = Employee
    template_name = 'employees/employee_delete.html'
    success_url = reverse_lazy('index')
