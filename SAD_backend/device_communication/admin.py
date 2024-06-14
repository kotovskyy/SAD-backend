from django.contrib import admin
from device_communication.models import Device, Measurement, Device_type, Setting_type, Setting, Measurement_type

# Register your models here.
admin.site.register([Device, Measurement, Device_type, Setting_type, Setting, Measurement_type])
