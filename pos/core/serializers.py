from django.contrib.auth.models import User
from rest_framework import serializers

from core.models.customer import Customer
from core.models.invoice import Invoice, InvoiceModifier
from core.models.modifier import Modifier

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    
    id = serializers.IntegerField()
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    full_name = serializers.CharField(source='user.get_full_name', read_only=True)
    identifier = serializers.CharField(read_only=True)
    email = serializers.EmailField(source='user.email')

    class Meta:
        model = Customer
        exclude = ('user', )

    def create(self, validated_data):
        user_data =  validated_data.pop('user')
        user_data['username'] = user_data['email']
        user = User.objects.create(**user_data)
        validated_data['user'] = user
        return Customer.objects.create(**validated_data)


class InvoiceSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField()
    customer = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all())
    customer_identifier = serializers.CharField(source='customer.identifier', read_only=True)

    class Meta:
        model = Invoice        


class InvoiceModifierSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = InvoiceModifier


class ModifierSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Modifier
