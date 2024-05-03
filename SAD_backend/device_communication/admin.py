from django.contrib import admin
from device_communication.models import Device, Measurement

# Register your models here.
admin.site.register([Device, Measurement])
