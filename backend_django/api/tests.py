from django.test import TestCase
from .models import Service, Product, Contact

class ServiceTest(TestCase):
    def test_create_service(self):
        service = Service.objects.create(name="TestService", description="Testing Service", price=100)
        self.assertEqual(service.name, "TestService")

class ProductTest(TestCase):
    def test_create_product(self):
        product = Product.objects.create(name="TestProduct", description="Testing Product", price=50, stock=10)
        self.assertEqual(product.stock, 10)

class ContactTest(TestCase):
    def test_create_contact(self):
        contact = Contact.objects.create(name="John Doe", email="contact@arcaoexdi.com")
        self.assertEqual(contact.email, "contact@arcaoexdi.com")