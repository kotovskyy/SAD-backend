from django.shortcuts import render
from rest_framework import viewsets
from device_communication.models import Device, Measurement
from front_communication.models import User
from API.serializers import DeviceSerializer, MeasurementSerializer, UserSerializer


class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


class MeasurementViewSet(viewsets.ModelViewSet):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
