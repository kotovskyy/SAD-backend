from django.contrib import admin
from device_communication.models import Device, Measurement, Device_type, Setting_type, Setting, Measurement_type

# Custom ModelAdmin classes for each model
class DeviceTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'device_type')

class DeviceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user', 'type', 'mac_address')

class SettingTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'unit')

class SettingAdmin(admin.ModelAdmin):
    list_display = ('id', 'device', 'type', 'value')

class MeasurementTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'unit')

class MeasurementAdmin(admin.ModelAdmin):
    list_display = ('id', 'device', 'timestamp', 'type', 'value')

# Register each model with its custom ModelAdmin class
admin.site.register(Device_type, DeviceTypeAdmin)
admin.site.register(Device, DeviceAdmin)
admin.site.register(Setting_type, SettingTypeAdmin)
admin.site.register(Setting, SettingAdmin)
admin.site.register(Measurement_type, MeasurementTypeAdmin)
admin.site.register(Measurement, MeasurementAdmin)
