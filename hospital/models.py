from django.db import models


# Create your models here.
class Hospital(models.Model):
    name = models.CharField(max_length=64, verbose_name="نام")
    location = models.CharField(max_length=64, blank=True, verbose_name="آدرس")
    phone_number = models.IntegerField(verbose_name="شماره تماس", blank=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "بیمارستان"
        verbose_name_plural = "بیمارستان ها"
