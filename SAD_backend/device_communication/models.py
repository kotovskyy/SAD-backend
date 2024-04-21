from django.db import models

# Create your models here.
class Device(models.Model):
    device_name = models.CharField(max_length=100)
    mac_address = models.CharField(max_length=100)
    user_id = models.ForeignKey('front_communication.User', on_delete=models.CASCADE)
    sleep_time = models.TimeField(default='22:00:00')
    wake_time = models.TimeField(default='06:00:00')
    preferred_temperature = models.FloatField(default=19.0)

class Measurement(models.Model):
    device_id = models.ForeignKey(Device, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    temperature = models.FloatField()
    humidity = models.FloatField()
    light_intensity = models.IntegerField()