from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from employees.models import Employee


@python_2_unicode_compatible
class EmployeeClock(models.Model):
    timestamp = models.DateTimeField()
    employee = models.ForeignKey(Employee)
    date_created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return "{employee} - {timestamp}".format(
            employee=self.employee.name,
            timestamp=self.timestamp.strftime('%D %X')
            )
    
    
    #these are little helpers
    #for reporting and search
    @property
    def get_month(self):
        return self.timestamp.month
    
    @property
    def get_day(self):
        return self.timestap.day
    
    @property
    def get_year(self):
        return self.timestamp.year

    @property
    def get_time(self):
        return self.timestamp.time

    @property
    def get_name(self):
        return self.employee.name