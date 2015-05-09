from django.db import models


class Employee(models.Model):
    """
    Employee username is not used to log in an user.
    It is used to identify the employee clocking in.
    """
    
    username = models.TextField()
    name = models.TextField()


    def __unicode__(self):
        return self.username