import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.db import models
from django.db.models import Max
from django.utils import timezone
from django.utils.datetime_safe import datetime
from django_countries.fields import CountryField
from stdimage import StdImageField


def generate_next_emp_no():
    return 1 if Employee.objects.all().count() == 0 else Employee.objects.all().aggregate(Max('emp_no'))['emp_no__max'] + 1


def upload_path_handler(self, filename):
    return u'profile/user_{id}/{file}'.format(id=self.pk, file=filename)


class LocalFileSystemStorage(FileSystemStorage):

    def get_available_name(self, name, max_length=None):
        if os.path.exists(self.path(name)):
            os.remove(self.path(name))
        return name


fs = LocalFileSystemStorage()


class Employee(models.Model):

    EMPLOYEE_TYPES = (
        ('MEM', 'Member'),
        ('AFF', 'Affiliate'),
        ('RET', 'Retired'),
        ('KIA', 'Killed in action'),
        ('PRE', 'President'),
        ('SEC', 'Secretary'),
        ('CFO', 'Chief Financial Officer'),
    )
    EMPLOYEE_DICT = {
        'MEM': 'Member-Owner',
        'AFF': 'Affiliate',
        'RET': 'Retired',
        'KIA': 'Killed in action',
        'PRE': 'President',
        'SEC': 'Secretary',
        'CFO': 'Chief Financial Officer',
    }

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
    ACTIVITY_DICT = {
        'HUN': 'Bounty Hunting',
        'ENG': 'Engineering',
        'EXP': 'Exploration',
        'FRE': 'Freelancing',
        'INF': 'Infiltration',
        'PIR': 'Piracy',
        'RES': 'Resources',
        'SCO': 'Scouting',
        'SEC': 'Security',
        'SMU': 'Smuggling',
        'SOC': 'Social',
        'TRD': 'Trading',
        'TRN': 'Transport',
    }

    emp_no = models.IntegerField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    type = models.CharField(max_length=3, choices=EMPLOYEE_TYPES, default='AFF')
    callsign = models.CharField(max_length=255)
    rsi_url = models.URLField(default='https://robertsspaceindustries.com/citizens/croberts68')
    birth_date = models.DateField(default=datetime(1980, 1, 1))
    hire_date = models.DateTimeField(default=timezone.now, blank=True)
    country = CountryField(blank_label='(select country)')
    primary_activity = models.CharField(max_length=3, choices=ACTIVITY_CHOICES, default='RES')
    secondary_activity = models.CharField(max_length=3, choices=ACTIVITY_CHOICES, default='TRD')
    bio = models.TextField(max_length=1000, blank=True)
    image = StdImageField(upload_to=upload_path_handler, storage=fs, null=True, blank=True, max_length=255, variations={
        'large': (400, 400),
        'thumbnail': (100,100, True),
        'medium': (200, 200),
    })

    def __str__(self):
        return "%s %s" % (self.user.first_name, self.user.last_name)

