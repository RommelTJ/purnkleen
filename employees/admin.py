from django.contrib import admin

from .models import Employee


class TypeFilter(admin.SimpleListFilter):
    title = 'Employee Type'
    parameter_name = 'type'

    def lookups(self, request, model_admin):
        return (
            ('MEM', 'Members'),
            ('AFF', 'Affiliates'),
        )

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(type__exact=self.value())
        else:
            return queryset


class EmployeeAdmin(admin.ModelAdmin):
    search_fields = ('emp_no', 'first_name', 'last_name', 'hire_date',)
    list_display = ('emp_no', 'first_name', 'last_name', 'type', 'hire_date',)
    list_display_links = ('emp_no',)
    list_filter = ('hire_date', TypeFilter,)
    save_on_top = True
    actions_on_bottom = False
    list_per_page = 10

    def first_name(self, obj):
        return obj.user.first_name

    def last_name(self, obj):
        return obj.user.last_name

    class Meta:
        model = Employee


admin.site.register(Employee, EmployeeAdmin)
