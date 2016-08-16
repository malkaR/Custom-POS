from django.contrib.auth.models import User
from rest_framework import viewsets

from core.serializers import UserSerializer, CustomerSerializer, InvoiceSerializer, ModifierSerializer
from core.models.customer import Customer
from core.models.invoice import Invoice
from core.models.modifier import Modifier


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Customer.objects.all().order_by('-user__date_joined')
    serializer_class = CustomerSerializer


class InvoiceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Invoice.objects.all().order_by('-timestamp')
    serializer_class = InvoiceSerializer


class ModifierViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Modifier.objects.all().order_by('-price')
    serializer_class = ModifierSerializer

