from django.db import models

# Create your models here.
class Device(models.Model):
    StatusChoises={
        ('س','سالم'),
        ('خ','خراب')
    }
    name = models.CharField(max_length=64, verbose_name= "نام")
    model = models.CharField(max_length=64, verbose_name= "مدل")
    brand = models.CharField(max_length=32, verbose_name= "برند")
    status = models.CharField(max_length=10, choices=StatusChoises, verbose_name="وضعیت")
    data_created = models.DateTimeField(auto_now_add=True)
    regular_checks = models.PositiveIntegerField()
    
    
    def __str__(self):
        return f"{self.name} {self.model}"
    
    class Meta:
        verbose_name = "دستگاه"
        verbose_name_plural = "دستگاه ها"
    #    ordering = ['regular_checks', '-status']
