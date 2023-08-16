from django.urls import path
from devices import views

app_name = "devices"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:device_id>", views.device, name="device"),
    path("create/", views.create, name="create"),
    path("edit/<int:device_id>", views.edit, name="edit"),
]
