from django.db import models
from employees.models import Employee


class EmployeeClock(models.Model):
    timestamp = models.DateTimeField()
    employee = models.ForeignKey(Employee)
    date_created = models.DateTimeField(auto_now_add=True)


    def __unicode__(self):
        return "{employee} - {timestamp}".format(
            employee=self.employee.name,
            timestamp=self.timestamp.strftime('%D %X')
            )
    
    
    #these are little helpers
    #for reporting and search
    @property
    def month(self):
        return self.timestamp.month
    
    
    @property
    def day(self):
        return self.timestap.day
    
    
    @property
    def year(self):
        return self.timestamp.year