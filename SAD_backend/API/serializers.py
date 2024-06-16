from rest_framework import serializers
from device_communication.models import (
    Device,
    Measurement,
    Device_type,
    Setting_type,
    Setting,
    Measurement_type,
)
from front_communication.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {"password": {"write_only": True}}


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True, validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password",
            "password2",
        )

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )
        return attrs

    def create(self, validated_data):
        user = User(
            username=validated_data["username"],
            email=validated_data["email"],
        )
        user.set_password(validated_data["password"])
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        if email and password:
            try:
                user = User.objects.get(email=email)
                user = authenticate(username=user.username, password=password)
            except User.DoesNotExist:
                user = None

            if user:
                attrs["user"] = user
                return attrs
            else:
                raise serializers.ValidationError("Invalid credentials")
        else:
            raise serializers.ValidationError("Must include 'email' and 'password'")


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = "__all__"
        extra_kwargs = {"type": {"required": True}, "user": {"required": False}}
    
    def __create_settings(self, device):
        default_settings = [
            #Sleep Assistant Device
            {"Temperature": 19.0,
            "Sleep time": 700.0,
            "Wake time": 2200.0,
            "Humidity": 50.0
            },

            #add new default settings here
        ]

        device_default_settings = default_settings[device.type.id-1]

        for setting_name in device_default_settings:
            setting_type = Setting_type.objects.get(name = setting_name)
            setting_default_value = device_default_settings[setting_name]
            Setting.objects.create(device=device, type=setting_type, value=setting_default_value)

    def create(self, validated_data):
        user = self.context["request"].user
        device = Device.objects.create(user=user, **validated_data)

        self.__create_settings(device)
        return device


class Device_typeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device_type
        fields = "__all__"


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = "__all__"
        extra_kwargs = {"type": {"required": True}}


class Measurement_typeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement_type
        fields = "__all__"


class SettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Setting
        fields = "__all__"
        extra_kwargs = {"type": {"required": True}}


class Setting_typeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Setting_type
        fields = "__all__"
