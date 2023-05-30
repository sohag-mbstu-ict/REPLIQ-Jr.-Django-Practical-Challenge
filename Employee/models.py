from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    name = models.CharField(max_length=100)

class Device(models.Model):
    name = models.CharField(max_length=100)
    condition = models.TextField()
    is_checked_out = models.BooleanField(default=False)
    checkout_time = models.DateTimeField(null=True, blank=True)
    return_time = models.DateTimeField(null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

class DeviceLog(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    condition = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
