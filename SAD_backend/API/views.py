from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authtoken.views import ObtainAuthToken
from device_communication.models import (
    Device,
    Measurement,
    Device_type,
    Setting_type,
    Setting,
    Measurement_type,
)
from front_communication.models import User
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from API.serializers import (
    DeviceSerializer,
    MeasurementSerializer,
    UserSerializer,
    Device_typeSerializer,
    Setting_typeSerializer,
    SettingSerializer,
    Measurement_typeSerializer,
    RegisterSerializer,
    LoginSerializer,
)


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        response.data["user_id"] = request.user.id
        return response


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=["post"], permission_classes=[AllowAny])
    def register(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"success": "User registered successfully"},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=["post"], permission_classes=[AllowAny])
    def login(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data["user"]
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeviceViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


class Device_typeViewSet(viewsets.ModelViewSet):
    queryset = Device_type.objects.all()
    serializer_class = Device_typeSerializer


class MeasurementViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer


class Measurement_typeViewSet(viewsets.ModelViewSet):
    queryset = Measurement_type.objects.all()
    serializer_class = Measurement_typeSerializer


class SettingViewSet(viewsets.ModelViewSet):
    queryset = Setting.objects.all()
    serializer_class = SettingSerializer


class Setting_typeViewSet(viewsets.ModelViewSet):
    queryset = Setting_type.objects.all()
    serializer_class = Setting_typeSerializer
