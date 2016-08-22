from __future__ import unicode_literals

from django.db import models

class Modifier(models.Model):
    
    description = models.CharField(max_length=150, blank=False)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    priced_by_weight = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    # commonly_used = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ['description', 'price', 'priced_by_weight']

    def delete(self, *args, **kwargs):
        self.active = False
        self.save()

    def activate(self):
        self.active = True
        self.save()

    def __unicode__(self):
        return '{0} - {1}'.format(self.description, self.price)

    def __str__(self):
        return self.__unicode__()
