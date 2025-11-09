# Create serializers for the Servicio, Producto, and Contacto models for API representation in format JSON.
from rest_framework import serializers
from .models import Servicio, Producto, Contacto

class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class ContactoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacto
        fields = '__all__'
