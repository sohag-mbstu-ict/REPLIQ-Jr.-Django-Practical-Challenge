from django.contrib import admin

# Register your models here.
from .models import Company,Device,DeviceLog
admin.site.register(Company)
admin.site.register(Device)
admin.site.register(DeviceLog)


