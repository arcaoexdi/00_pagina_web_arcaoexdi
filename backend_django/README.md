📘 Backend Documentation – Company Website (Django + DRF)
1. 📦 Project Overview
This backend provides a RESTful API for a company website. It manages:

Services offered by the company

Products/Catalog

Contact messages from clients

The API is built with Django 5.2.8 and Django REST Framework 3.16.1, documented with Swagger/Redoc via drf-yasg, and secured with JWT authentication using djangorestframework-simplejwt.

2. ⚙️ Dependencies
Installed packages (via pip freeze):

Django==5.2.8 → Core framework

djangorestframework==3.16.1 → REST API support

django-cors-headers==4.9.0 → Allow Angular frontend to connect

drf-yasg==1.21.11 → Swagger/OpenAPI documentation

python-decouple==3.8 → Environment variables management

PyYAML==6.0.3 → Schema serialization

sqlparse==0.5.3 → SQL parsing (Django internal)

djangorestframework-simplejwt → JWT authentication (added manually)

3. 🏗️ Project Structure
Código
backend_django/
├── company_core/        # Main project
│   ├── settings.py      # Configurations
│   ├── urls.py          # Global routes
│   ├── wsgi.py / asgi.py
├── api/                 # API app
│   ├── models.py        # Database models
│   ├── serializers.py   # JSON serializers
│   ├── views.py         # ViewSets (CRUD logic)
│   ├── urls.py          # API routes
├── manage.py
4. ⚙️ Settings Configuration
In company_core/settings.py:

python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'rest_framework',
    'corsheaders',
    'api',
    'drf_yasg',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    ...
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:4200",  # Angular dev server
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}
5. 🗄️ Models (api/models.py)
python
class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
6. 🔄 Serializers (api/serializers.py)
python
class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
7. 📡 Views (api/views.py)
python
class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
8. 🌐 Routes
api/urls.py
python
router = routers.DefaultRouter()
router.register(r'services', ServiceViewSet)
router.register(r'catalog', ProductViewSet)
router.register(r'contacts', ContactViewSet)

urlpatterns = router.urls
company_core/urls.py
python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),

    # JWT Authentication
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Swagger & Redoc
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
9. 🔒 Authentication (JWT)
Login: POST /api/token/ → returns access and refresh tokens.

Refresh: POST /api/token/refresh/ → renews access token.

Usage: Angular must send Authorization: Bearer <access_token> in headers.

10. 📖 Documentation (Swagger/Redoc)
http://127.0.0.1:8000/swagger/ → Interactive API testing.

http://127.0.0.1:8000/redoc/ → Clean documentation view.

11. 🧪 Testing
Example in api/tests.py:

python
class ServiceTest(TestCase):
    def test_create_service(self):
        service = Service.objects.create(name="Test", description="Testing", price=100)
        self.assertEqual(service.name, "Test")
Run tests:

bash
python manage.py test
12. 🚀 Next Steps for Production
Switch DB to Postgres.

Add filters, pagination, search (django-filter).

Configure media storage for product images.

Deploy with Gunicorn + Nginx or cloud services.

Add logging and monitoring.

✅ Summary
Your backend is:

Fully functional with CRUD endpoints.

Secured with JWT authentication.

Documented with Swagger/Redoc.

Ready to connect with Angular frontend.