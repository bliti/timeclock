from django.db import models
from employees.models import Employee


class Clock(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    employee = models.ForeignKey(Employee)


    def __unicode__(self):
        return self.timestamp    