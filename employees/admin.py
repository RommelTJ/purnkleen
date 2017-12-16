from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Employee
from .forms import EmployeeForm


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
    form = EmployeeForm
    search_fields = ('emp_no', 'first_name', 'last_name', 'hire_date',)
    list_display = ('image_thumbnail', 'emp_no', 'first_name', 'last_name', 'type', 'hire_date',)
    list_display_links = ('emp_no',)
    list_filter = ('hire_date', TypeFilter,)
    save_on_top = True
    actions_on_bottom = False
    list_per_page = 10
    placeholder = '/media/profile/star_citizen_marine_100x100.jpg'

    def image_thumbnail(self, obj):
        return mark_safe('<img src="%s" />' % obj.image.thumbnail.url if obj.image else '<img src="%s" />' % self.placeholder)

    image_thumbnail.short_description = 'Profile Image'

    def first_name(self, obj):
        return obj.user.first_name

    def last_name(self, obj):
        return obj.user.last_name

    class Meta:
        model = Employee


admin.site.register(Employee, EmployeeAdmin)
