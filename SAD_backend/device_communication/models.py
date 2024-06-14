from django.db import models
from django.utils import timezone

class Device_type(models.Model):
    id = models.SmallAutoField(primary_key=True)
    device_type = models.CharField(max_length=100)

    class Meta:
        db_table = 'device_type'

# Create your models here.
class Device(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(
        'front_communication.User',
        related_name='devices',
        on_delete=models.CASCADE
    )
    type = models.ForeignKey(
        Device_type,
        related_name='devices',
        on_delete=models.CASCADE,
        null=True
    )
    mac_address = models.CharField(max_length=17)

    class Meta:
        db_table = 'device'

class Setting_type(models.Model):
    id = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=20)
    unit = models.CharField(max_length=10)

    class Meta:
        db_table = 'setting_type'

class Setting(models.Model):
    device = models.ForeignKey(
        Device,
        related_name='settings',
        on_delete=models.CASCADE
    )
    type = models.ForeignKey(
        Setting_type,
        related_name='settings',
        on_delete=models.CASCADE,
        null=True
    )
    value = models.FloatField()

    class Meta:
        db_table = 'setting'
    

class Measurement_type(models.Model):
    id = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=20)
    unit = models.CharField(max_length=10)

    class Meta:
        db_table = 'measurement_type'

class Measurement(models.Model):
    device = models.ForeignKey(
        Device,
        related_name='measurements',    
        on_delete=models.CASCADE
    )
    timestamp = models.DateTimeField(default=timezone.now)
    type = models.ForeignKey(
        Measurement_type,
        related_name='measurements',
        on_delete=models.CASCADE,
        null=True
    )
    value = models.FloatField()

    class Meta:
        db_table = 'measurement'
