from rest_framework import routers
from .views import ServiceViewSet, ProductViewSet, ContactViewSet

router = routers.DefaultRouter()
# Route of the API endpoints services
router.register(r'services', ServiceViewSet)

# Route of the API endpoints products
router.register(r'catalog', ProductViewSet) 

# Route of the API endpoints contacts
router.register(r'contacts', ContactViewSet)

# Final URL patterns
urlpatterns = router.urls
