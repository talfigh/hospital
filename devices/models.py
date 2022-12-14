from django.db import models

# Create your models here.
class DeviceName(models.Model):
    device_name = models.CharField(unique=True,max_length=64, verbose_name= "نام")
    
    def __str__(self):
        return f"{self.device_name}"
    
    class Meta:
        verbose_name = "نام"
        verbose_name_plural = "نام ها"

class ModelName(models.Model):
    model_name = models.CharField(unique=True,max_length=64, verbose_name= "مدل")
    
    def __str__(self):
        return f"{self.model_name}"
        
    class Meta:
        verbose_name = "مدل"
        verbose_name_plural = "مدل ها"

class StatusName(models.Model):
    status_name = models.CharField(unique=True,max_length=64, verbose_name= "وضعیت")
    
    def __str__(self):
        return f"{self.status_name}"
        
    class Meta:
        verbose_name = "وضعیت"
        verbose_name_plural = "وضعیت ها"

class GroupName(models.Model):
    group_name = models.CharField(unique=True,max_length=64, verbose_name= "گروه")
    
    def __str__(self):
        return f"{self.group_name}"
        
    class Meta:
        verbose_name = "گروه"
        verbose_name_plural = "گروه ها"

class BrandName(models.Model):
    brand_name = models.CharField(unique=True,max_length=64, verbose_name= "مارک")
    
    def __str__(self):
        return f"{self.brand_name}"
        
    class Meta:
        verbose_name = "مارک"
        verbose_name_plural = "مارک ها"


class Device(models.Model):
    name = models.ForeignKey(DeviceName, on_delete=models.CASCADE, related_name="Dname", verbose_name= "نام")
    model = models.ForeignKey(ModelName, on_delete=models.CASCADE, related_name="Mname", verbose_name= "مدل")
    status = models.ForeignKey(StatusName, on_delete=models.CASCADE, related_name="Sname", verbose_name= "وضعیت")
    group = models.ForeignKey(GroupName, on_delete=models.CASCADE, related_name="Gname",verbose_name = "گروه")
    brand = models.ForeignKey(BrandName, on_delete=models.CASCADE, related_name="Bname", verbose_name= "مارک")
    data_created = models.DateTimeField(auto_now_add=True)
    regular_checks = models.PositiveIntegerField( verbose_name= "دوره های زمانی سرویس(برحسب ماه)")
    
    
    def __str__(self):
        return f"{self.name} {self.model}"
    
    class Meta:
        verbose_name = "دستگاه"
        verbose_name_plural = "دستگاه ها"
    #    ordering = ['regular_checks', '-status']




