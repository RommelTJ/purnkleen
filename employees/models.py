from django.conf import settings
from django.db import models
from django.db.models import Max
from django.utils import timezone
from django.utils.datetime_safe import datetime
from django_countries.fields import CountryField


def generate_next_emp_no():
    return 1 if Employee.objects.all().count() == 0 else Employee.objects.all().aggregate(Max('emp_no'))['emp_no__max'] + 1


class Employee(models.Model):

    EMPLOYEE_TYPES = (
        ('MEM', 'Member'),
        ('AFF', 'Affiliate'),
        ('RET', 'Retired'),
        ('KIA', 'Killed in action'),
    )

    ACTIVITY_CHOICES = (
        ('HUN', 'Bounty Hunting'),
        ('ENG', 'Engineering'),
        ('EXP', 'Exploration'),
        ('FRE', 'Freelancing'),
        ('INF', 'Infiltration'),
        ('PIR', 'Piracy'),
        ('RES', 'Resources'),
        ('SCO', 'Scouting'),
        ('SEC', 'Security'),
        ('SMU', 'Smuggling'),
        ('SOC', 'Social'),
        ('TRD', 'Trading'),
        ('TRN', 'Transport'),
    )

    emp_no = models.IntegerField(primary_key=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    type = models.CharField(max_length=3, choices=EMPLOYEE_TYPES, default='AFF')
    callsign = models.CharField(max_length=255)
    rsi_url = models.URLField(default='https://robertsspaceindustries.com/citizens/croberts68')
    birth_date = models.DateField(default=datetime(1980, 1, 1))
    hire_date = models.DateTimeField(default=timezone.now, blank=True)
    country = CountryField(blank_label='(select country)')
    primary_activity = models.CharField(max_length=3, choices=ACTIVITY_CHOICES, default='RES')
    secondary_activity = models.CharField(max_length=3, choices=ACTIVITY_CHOICES, default='TRD')

    def __str__(self):
        return "%s %s" % (self.user.first_name, self.user.last_name)
