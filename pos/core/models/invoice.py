from __future__ import unicode_literals

from django.db import models

from core.models.customer import Customer
from core.models.modifier import Modifier


class Invoice(models.Model):

    timestamp = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer)
    preferences = models.TextField(blank=True)
    modifiers = models.ManyToManyField(Modifier, blank=True, through='InvoiceModifier')
    cost = models.DecimalField(max_digits=10, decimal_places=2, editable=False, default=0)

    class Meta:
        ordering = ['timestamp']

    def save(self, *args, **kwargs):
        super(Invoice, self).save(*args, **kwargs)
        self.update_cost()

    def update_cost(self):
        self.cost = sum([m.cost for m in InvoiceModifier.objects.filter(invoice=self)])
        super(Invoice, self).save(update_fields=['cost'])

    def __unicode__(self):
        return '{0}, {1}'.format(self.customer.identifier, self.timestamp.date())

    def __str__(self):
        return self.__unicode__()


class InvoiceModifier(models.Model):
    invoice = models.ForeignKey(Invoice)
    modifier = models.ForeignKey(Modifier)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    cost = models.DecimalField(max_digits=10, decimal_places=2, editable=False, default=0)
    preferences = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        self.cost = self.modifier.price * self.quantity
        super(InvoiceModifier, self).save(*args, **kwargs)
        self.invoice.update_cost()

    def delete(self, *args, **kwargs):
        deleted = super(InvoiceModifier, self).delete(*args, **kwargs)
        self.invoice.update_cost()
        return deleted
