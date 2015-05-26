from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models


@python_2_unicode_compatible
class Organization(models.Model):
    """
    The organization object refers to
    the business, company or group
    that the employee belongs to.
    
    The password is not encrypted
    for the following reasons:
        - to give the admin the ability to see and share the password
        - to allow the admin to forget the password
        - no personal employee information is shown in any screen where
          password allows access to.
        - no business information is shown in any screen where the password
          allows access to.
        - In order for an employee to clock it must user their username,
          which is also not displayed anywhere publicly.
    
    The critical data is protected by the standard Django admin encrypted password.
    Only the Django admin has access to it.
    
    """

    name = models.TextField(unique=True)
    password = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.name