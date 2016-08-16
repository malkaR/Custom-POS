from __future__ import unicode_literals

from django.db import models

class Modifier(models.Model):
    
    description = models.CharField(max_length=150, blank=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    active = models.BooleanField(default=True)
