from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

class Customer(models.Model):
    
    user = models.OneToOneField(User)
    preferences = models.TextField(blank=True)

    @property
    def identifier(self):
        if self.user.first_name and self.user.last_name:
            return '{} {} - {}'.format(
                self.user.first_name, self.user.last_name, self.user.email)
        return self.user.email

    def __unicode__(self):
        return '{0}, {1}'.format(self.user.first_name, self.user.last_name)

    def __str__(self):
        return self.__unicode__()
