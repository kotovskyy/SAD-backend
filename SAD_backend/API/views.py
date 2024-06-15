from django.shortcuts import render
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from API.permissions import IsOwnerOrReadOnly
from front_communication.models import User
from device_communication.models import (
    Device,
    Measurement,
    Device_type,
    Setting_type,
    Setting,
    Measurement_type,
)
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

    def get_permissions(self):
        if self.action in ['retrieve', 'update', 'partial_update', 'destroy']:
            return [IsAuthenticated(), IsOwnerOrReadOnly()]
        elif self.action in ['register', 'login']:
            return [AllowAny()]
        return [IsAuthenticated()]
    
    def get_queryset(self):
        user = self.request.user
        return User.objects.filter(id=user.id)


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
    serializer_class = DeviceSerializer
    permission_classes = [IsAuthenticated]  # Ensure user is authenticated and owns the device

    def get_queryset(self):
        user = self.request.user
        return Device.objects.filter(user=user)
    
    # def destroy(self, request, *args, **kwargs):
    #     return super().destroy(request, *args, **kwargs)
    



class Device_typeViewSet(viewsets.ModelViewSet):
    queryset = Device_type.objects.all()
    serializer_class = Device_typeSerializer


class MeasurementViewSet(viewsets.ModelViewSet):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        device_id = self.request.query_params.get("device")
        if device_id:
            return Measurement.objects.filter(device__user=user, device_id=device_id)
        return Measurement.objects.filter(device__user=user)


class Measurement_typeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Measurement_type.objects.all()
    serializer_class = Measurement_typeSerializer


class SettingViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Setting.objects.all()
    serializer_class = SettingSerializer

    def list(self, request):
        user = request.user
        device_id = request.query_params.get("device")
        if device_id:
            queryset = Setting.objects.filter(device__user=user, device=device_id)
        else:
            queryset = Setting.objects.filter(device__user=user)
        serializer = SettingSerializer(queryset, many=True)
        return Response(serializer.data)


class Setting_typeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Setting_type.objects.all()
    serializer_class = Setting_typeSerializer
