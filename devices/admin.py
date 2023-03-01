from django.contrib import admin

from .models import Device,DeviceName,ModelName,StatusName,BrandName,GroupName,DeviceLog
from users.models import Personnel
from hospital.models import Hospital
# Register your models here.

admin.site.register(Device)
admin.site.register(DeviceName)
admin.site.register(ModelName)
admin.site.register(StatusName)
admin.site.register(BrandName)
admin.site.register(GroupName)
admin.site.register(Personnel)
admin.site.register(Hospital)
admin.site.register(DeviceLog)





