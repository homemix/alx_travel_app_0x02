from rest_framework.routers import DefaultRouter

from .views import BookingViewSet, PropertyViewSet

router = DefaultRouter()
router.register(r'property', PropertyViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = router.urls
