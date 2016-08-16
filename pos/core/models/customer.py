from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

class Customer(models.Model):
    
    user = models.OneToOneField(User)
    preferences = models.TextField()

    def __unicode__(self):
        return self.user.first_name + self.user.last_name

    def __str__(self):
        return self.__unicode__()
