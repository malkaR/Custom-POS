from django.contrib.auth.models import User
from rest_framework import serializers

from core.models.customer import Customer
from core.models.invoice import Invoice
from core.models.modifier import Modifier

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer


class InvoiceSerializer(serializers.HyperlinkedModelSerializer):
    customer = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all())
    class Meta:
        model = Invoice


class ModifierSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Modifier
