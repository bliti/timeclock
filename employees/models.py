from django.db import models
from organizations.models import Organization


class Employee(models.Model):
    """
    Employee username is not used to log in an user.
    It is used to identify the employee clocking in.
    
    identifier field allows for the employee to have
    an external method to which identify it.
    Like the Social Security Number (SSN),
    which is used in a lot of companies
    to identify their employees and for reports.
    Its optional
    """
    
    username = models.TextField(unique=True)
    name = models.TextField()
    identifier = models.CharField(max_length=256,null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    organization = models.ForeignKey(Organization)


    def __unicode__(self):
        return self.username