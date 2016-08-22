from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from core.serializers import (
    UserSerializer, CustomerSerializer, InvoiceSerializer,
    InvoiceModifierSerializer, ModifierSerializer
)
from core.models.customer import Customer
from core.models.invoice import Invoice, InvoiceModifier
from core.models.modifier import Modifier


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all().order_by('user__last_name')
    serializer_class = CustomerSerializer

    @detail_route(methods=['get'])
    def invoices(self, request, pk=None):
        """Return invoices for a customer."""
        customer = self.get_object()
        invoices_queryset = Invoice.objects.filter(customer=customer)
        serializer = InvoiceSerializer(
            invoices_queryset, context={'request': request}, many=True)
        return Response(serializer.data)

        
class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer


class InvoiceModifierViewSet(viewsets.ModelViewSet):
    queryset = InvoiceModifier.objects.all()
    serializer_class = InvoiceModifierSerializer

class ModifierViewSet(viewsets.ModelViewSet):
    queryset = Modifier.objects.all().order_by('-price')
    serializer_class = ModifierSerializer

