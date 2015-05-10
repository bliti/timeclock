from django.db import models
from employees.models import Employee


class EmployeeClock(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    employee = models.ForeignKey(Employee)


    def __unicode__(self):
        return "{employee} - {timestamp}".format(
            employee=self.employee.name,
            timestamp=self.timestamp.strftime('%D %I:%X')
            )