from django.shortcuts import render
from .models import Device
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import CreateForm

# Create your views here.
@login_required
def index(request):
    return render(request, "devices/index.html", {
        "devices": Device.objects.all()
    })

def device(request, device_id):
    device = Device.objects.get(pk=device_id)
    return render(request, "devices/device.html",{
        "device": device
    })

def create(request):
    context = {}
    form = CreateForm(request.POST or None)   

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("devices:index"))
    
    context['form']= form
    return render(request, "devices/create.html",context)

    