from django.db import models
from hospital.models import Hospital
from django.contrib.auth.models import User

# Create your models here.
class Personnel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, default="", related_name="person")
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, verbose_name="نام بیمارستان")
    
    def __str__(self):
        return f"{self.user}: {self.hospital}"   
    
    class Meta:
        verbose_name = "پرسنل"
        verbose_name_plural = "پرسنل"