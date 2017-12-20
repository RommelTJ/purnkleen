from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from .models import Employee, generate_next_emp_no

User = get_user_model()


class TestEmployee(TestCase):
    def setUp(self):
        User.objects.create(username='rommel', first_name='Rommel', last_name='Rico')
        User.objects.create(username='johndoe', first_name='John', last_name='Doe')
        Employee.objects.create(emp_no=1, user=User.objects.first(), callsign='Test', country='US')

    def test_employee_create(self):
        obj1 = Employee.objects.create(
            emp_no=generate_next_emp_no(),
            user=User.objects.first(),
            callsign='Boomer',
            country='US'
        )
        obj2 = Employee.objects.create(
            emp_no=generate_next_emp_no(),
            user=User.objects.get(username='johndoe'),
            callsign='Jonny',
            country='US'
        )
        self.assertTrue(obj1.emp_no == 2)
        self.assertTrue(obj1.user.first_name == "Rommel")
        self.assertTrue(obj1.callsign == "Boomer")

        self.assertTrue(obj2.emp_no == 3)
        self.assertTrue(obj2.user.first_name == "John")
        self.assertTrue(obj2.callsign == "Jonny")

    def test_employee_defaults(self):
        obj = Employee.objects.first()
        self.assertTrue(obj.type == 'AFF')
        self.assertTrue(obj.rsi_url == 'https://robertsspaceindustries.com/citizens/croberts68')
        self.assertIsNotNone(obj.birth_date)
        self.assertIsNotNone(obj.hire_date)
        self.assertTrue(obj.primary_activity == 'RES')
        self.assertTrue(obj.secondary_activity == 'TRD')
        self.assertTrue(obj.bio == '')
        self.assertIsNotNone(obj.image)

    def test_employee_url(self):
        obj = Employee.objects.create(
            emp_no=generate_next_emp_no(),
            user=User.objects.first(),
            callsign='Boomer',
            country='US'
        )
        absolute_url = reverse('employee:detail', kwargs={'pk': obj.emp_no})
        self.assertEqual(obj.get_absolute_url(), absolute_url)
