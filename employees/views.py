from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView

from .forms import EmployeeForm
from .mixins import UserOwnerMixin
from .models import Employee, generate_next_emp_no


class EmployeeCreateView(LoginRequiredMixin, CreateView):
    form_class = EmployeeForm
    template_name = 'employees/employee_create.html'

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
            self.object.type = 'AFF'  # All new employees start out as affiliates.
            self.object.save()
            return HttpResponseRedirect(reverse_lazy('employee:detail', kwargs={'pk': self.object.emp_no}))
        return render(request, self.template_name, {'form': form})

    def get_context_data(self):
        return {
            'employee': self.get_employee(),
        }

    def get_employee(self):
        qs = Employee.objects.filter(
            user__exact=self.request.user
        ).filter(
            type__in=["MEM","AFF", "PRE", "SEC", "CFO"]
        ).first()
        return qs


class EmployeeUpdateView(LoginRequiredMixin, UserOwnerMixin, UpdateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'employees/employee_update.html'

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
            return HttpResponseRedirect(reverse_lazy('employee:detail', kwargs={'pk': self.object.emp_no}))
        return render(request, self.template_name, {'form': form})


class EmployeeDeleteView(LoginRequiredMixin, UserOwnerMixin, DeleteView):
    model = Employee
    template_name = 'employees/employee_delete.html'
    success_url = reverse_lazy('index')


class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'employees/employee_detail.html'

    def get_context_data(self, **kwargs):
        context = super(EmployeeDetailView, self).get_context_data(**kwargs)
        is_owner = self.request.user == self.object.user
        context['is_owner'] = is_owner
        context['activity_dict'] = Employee.ACTIVITY_DICT
        context['employee_dict'] = Employee.EMPLOYEE_DICT
        return context


class EmployeeListView(ListView):
    model = Employee
    template_name = 'employees/employee_list.html'
    paginate_by = 10
    ordering = 'emp_no'
    queryset = Employee.objects.filter(type__in=["MEM", "AFF"])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(EmployeeListView, self).get_context_data()
        context['activity_dict'] = Employee.ACTIVITY_DICT
        context['employee_dict'] = Employee.EMPLOYEE_DICT
        context['president'] = self.get_president()
        context['secretary'] = self.get_secretary()
        context['cfo'] = self.get_cfo()
        return context

    def get_president(self):
        qs = Employee.objects.filter(type="PRE").first()  # There is only one President.
        return qs

    def get_secretary(self):
        qs = Employee.objects.filter(type="SEC").first()  # There is only one Secretary.
        return qs

    def get_cfo(self):
        qs = Employee.objects.filter(type="CFO").first()  # There is only one Chief Financial Officer.
        return qs


def employee_retire_view(request, **kwargs):
    if kwargs['pk'] is not None:
        emp_no = kwargs['pk']
        employee = Employee.objects.get(emp_no=emp_no)
        if request.user == employee.user:
            employee.type = 'RET'
            employee.save()
            return HttpResponseRedirect(reverse_lazy('employee:list'))
        return HttpResponseRedirect(reverse_lazy('employee:list'))
    return HttpResponseRedirect(reverse_lazy('employee:list'))


def employee_kia_view(request, **kwargs):
    if kwargs['pk'] is not None:
        emp_no = kwargs['pk']
        employee = Employee.objects.get(emp_no=emp_no)
        if request.user == employee.user:
            employee.type = 'KIA'
            employee.save()
            return HttpResponseRedirect(reverse_lazy('employee:list'))
        return HttpResponseRedirect(reverse_lazy('employee:list'))
    return HttpResponseRedirect(reverse_lazy('employee:list'))