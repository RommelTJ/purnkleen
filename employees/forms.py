from django import forms
from django_countries.widgets import CountrySelectWidget
from django.utils.safestring import mark_safe

from .models import Employee


class EmployeeImageFieldWidget(forms.widgets.FileInput):
    def __init__(self, placeholder='/media/profile/star_citizen_marine_400x400.jpg'):
        self.placeholder = placeholder
        super(EmployeeImageFieldWidget, self).__init__({})

    def render(self, name, value, attrs=None, **kwargs):
        image_html = '<img src="%s" />' % value.medium.url if value and hasattr(value, "url") else '<img src="%s" />' % self.placeholder
        return mark_safe("%s%s" % (image_html, super(EmployeeImageFieldWidget, self).render(name, value, attrs)))


class EmployeeForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Chris'}),
        required=True,
        label='First name',
        help_text="Don't enter your real name if you don't feel comfortable with this being public."
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Roberts'}),
        required=True,
        label='Last name'
    )
    callsign = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'RedOne'}),
        required=True,
        label='Callsign'
    )
    rsi_url = forms.URLField(
        widget=forms.URLInput(attrs={'placeholder': 'https://robertsspaceindustries.com/citizens/croberts68'}),
        required=True,
        label="RSI URL"
    )
    birth_date = forms.DateField(
        widget=forms.SelectDateWidget(years=range(1950, 2030)),
        help_text="Not required but used to wish you happy birthday."
    )
    image = forms.ImageField(
        label="Profile Image",
        widget=EmployeeImageFieldWidget(),
        required=False,
        help_text="Please upload a square 400x400 image."
    )

    def __str__(self):
        return '%s %s' % (self.user.first_name, self.user.last_name)

    class Meta:
        model = Employee
        fields = (
            'first_name',
            'last_name',
            'callsign',
            'image',
            'rsi_url',
            'primary_activity',
            'secondary_activity',
            'country',
            'birth_date',
            'bio',
        )
        widgets = {'country': CountrySelectWidget()}


class EmployeeAdminForm(EmployeeForm):
    class Meta:
        model = Employee
        fields = (
            'user',
            'callsign',
            'image',
            'type',
            'rsi_url',
            'primary_activity',
            'secondary_activity',
            'country',
            'birth_date',
            'bio',
        )
        widgets = {'country': CountrySelectWidget()}
