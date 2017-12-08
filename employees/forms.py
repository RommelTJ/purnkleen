from django import forms
from django_countries.widgets import CountrySelectWidget
from django.utils.datetime_safe import datetime

from .models import Employee


class EmployeeForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Chris'}),
        required=True,
        label='First name'
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
    birth_date = forms.DateField(widget=forms.SelectDateWidget(years=range(1950, 2025)), initial=datetime(1988, 1, 1))

    def __str__(self):
        return '%s %s' % (self.user.first_name, self.user.last_name)

    class Meta:
        model = Employee
        fields = (
            'first_name',
            'last_name',
            'callsign',
            'rsi_url',
            'primary_activity',
            'secondary_activity',
            'country',
            'birth_date',
        )
        widgets = {'country': CountrySelectWidget()}
