from django.contrib import admin

from .models import Device,DeviceName,ModelName,StatusName,BrandName,GroupName
# Register your models here.

admin.site.register(Device)
admin.site.register(DeviceName)
admin.site.register(ModelName)
admin.site.register(StatusName)
admin.site.register(BrandName)
admin.site.register(GroupName)




