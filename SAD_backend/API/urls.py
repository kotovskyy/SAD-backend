from django.urls import path, include
from rest_framework.routers import DefaultRouter
from API import views

router = DefaultRouter()
router.register(r'devices', views.DeviceViewSet, basename='device')
router.register(r'measurements', views.MeasurementViewSet, basename='measurement')

urlpatterns = [
    path('', include(router.urls)),
]
