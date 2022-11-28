from django.urls import path
from . import views 


app_name = "devices"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:device_id>", views.device, name="device"),
    path("create/", views.create, name="create"),
]