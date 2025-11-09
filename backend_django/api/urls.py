from django.urls import path
from rest_framework import routers
from .views import ServicioViewSet, ProductoViewSet, ContactoViewSet, inicio
from rest_framework.response import Response


router = routers.DefaultRouter()
router.register(r'servicios', ServicioViewSet)
router.register(r'catalogo', ProductoViewSet)
router.register(r'contacto', ContactoViewSet)

urlpatterns = [
    path('inicio/', inicio),   # <-- aquí agregamos la ruta manual
]

urlpatterns += router.urls
