from rest_framework import viewsets
from .models import Service, Product, Contact
from .serializers import ServiceSerializer, ProductSerializer, ContactSerializer

# View of the view of Service
class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    filterset_fields = ['name', 'price']

# View of the view of Product
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_fields = ['name', 'price', 'stock']

# View of the view of Contact
class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    filterset_fields = ['name', 'email']