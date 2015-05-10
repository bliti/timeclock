from django.db import models
from organizations.models import Organization


class Employee(models.Model):
    """
    Employee username is not used to log in an user.
    It is used to identify the employee clocking in.
    """
    
    username = models.TextField()
    name = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    organization = models.ForeignKey(Organization)


    def __unicode__(self):
        return self.username