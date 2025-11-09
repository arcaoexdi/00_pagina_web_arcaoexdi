from rest_framework import viewsets
from .models import Servicio, Producto, Contacto
from .serializers import ServicioSerializer, ProductoSerializer, ContactoSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def inicio(request):
    return Response({"mensaje": "Bienvenido a la API de Arca Oexdi"})


class ServicioViewSet(viewsets.ModelViewSet):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class ContactoViewSet(viewsets.ModelViewSet):
    queryset = Contacto.objects.all()
    serializer_class = ContactoSerializer
