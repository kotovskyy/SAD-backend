from django.urls import path, include
from rest_framework.routers import DefaultRouter
from API import views

router = DefaultRouter()
router.register(r"users", views.UserViewSet, basename="user")
router.register(r"devices", views.DeviceViewSet, basename="device")
router.register(r"device_types", views.Device_typeViewSet, basename="device_type")
router.register(r"measurements", views.MeasurementViewSet, basename="measurement")
router.register(
    r"measurement_types", views.Measurement_typeViewSet, basename="measurement_type"
)
router.register(r"settings", views.SettingViewSet, basename="setting")
router.register(r"setting_types", views.Setting_typeViewSet, basename="setting_type")


urlpatterns = [
    path("", include(router.urls)),
]
