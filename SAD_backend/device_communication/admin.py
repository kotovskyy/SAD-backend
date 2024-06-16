from django.contrib import admin
from device_communication.models import Device, Measurement, Device_type, Setting_type, Setting, Measurement_type

# Custom ModelAdmin classes for each model
class DeviceTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'device_type')

class DeviceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user', 'device_type_display', 'mac_address')

    @admin.display(description='Type')
    def device_type_display(self, obj):
        return obj.type.id, obj.type.device_type

class SettingTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'unit')

class SettingAdmin(admin.ModelAdmin):
    list_display = ('id', 'device_display', 'type_display', 'value')

    @admin.display(description='Device')
    def device_display(self, obj):
        return obj.device.name
    
    @admin.display(description='Type')
    def type_display(self, obj):
        return obj.type.id, obj.type.name

class MeasurementTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'unit')

class MeasurementAdmin(admin.ModelAdmin):
    list_display = ('id', 'device_display', 'timestamp', 'type_display', 'value')

    @admin.display(description='Device')
    def device_display(self, obj):
        return obj.device.name
    
    @admin.display(description='Type')
    def type_display(self, obj):
        return obj.type.id, obj.type.name

# Register each model with its custom ModelAdmin class
admin.site.register(Device_type, DeviceTypeAdmin)
admin.site.register(Device, DeviceAdmin)
admin.site.register(Setting_type, SettingTypeAdmin)
admin.site.register(Setting, SettingAdmin)
admin.site.register(Measurement_type, MeasurementTypeAdmin)
admin.site.register(Measurement, MeasurementAdmin)
