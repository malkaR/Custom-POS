from __future__ import unicode_literals

from django.db import models

from core.models.customer import Customer
from core.models.modifier import Modifier

class Invoice(models.Model):

    timestamp = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer)
    preferences = models.TextField(blank=True)
    modifiers = models.ManyToManyField(Modifier, blank=True)
