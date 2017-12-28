from rest_framework import serializers

from accounts.api.serializers import UserDisplaySerializer
from employees.models import Employee


class EmployeeModelSerializer(serializers.ModelSerializer):
    user = UserDisplaySerializer(read_only=True)

    class Meta:
        model = Employee
        fields = "__all__"


    # emp_no = models.IntegerField(primary_key=True)
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # type = models.CharField(max_length=3, choices=EMPLOYEE_TYPES, default='AFF')
    # callsign = models.CharField(max_length=255)
    # rsi_url = models.URLField(default='https://robertsspaceindustries.com/citizens/croberts68')
    # birth_date = models.DateField(default=datetime(1980, 1, 1))
    # hire_date = models.DateTimeField(default=timezone.now, blank=True)
    # country = CountryField(blank_label='(select country)')
    # primary_activity = models.CharField(max_length=3, choices=ACTIVITY_CHOICES, default='RES')
    # secondary_activity = models.CharField(max_length=3, choices=ACTIVITY_CHOICES, default='TRD')
    # bio = models.TextField(max_length=1000, blank=True)
    # image = StdImageField(upload_to=upload_path_handler, storage=fs, null=True, blank=True, max_length=255, variations={
    #     'large': (400, 400),
    #     'thumbnail': (100,100, True),
    #     'medium': (200, 200),
    # })