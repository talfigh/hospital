from django.shortcuts import render
from .models import Device, DeviceLog, DeviceName, ModelName
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from users.models import Personnel
from hospital.models import Hospital
from django.contrib.auth.models import User
import datetime
# from django.db.models import Q


from .forms import CreateForm, LogForm


# Create your views here.
#@login_required
def index(request):
    if request.user.is_authenticated:
        query = request.GET.get('q', '')

        user_id = request.user.id
        personnel = Personnel.objects.filter(user=user_id).first()
        hospital = personnel.hospital


        if query:
            # queryset = (Q(text__icontains=query))
            results = Device.objects.filter(name__icontains=query).distinct()

        else:
            results = Device.objects.filter(hospital = hospital)

        return render(request, 'devices/index.html', {"devices": results, "search_input": query})
    else:
        return HttpResponseRedirect(reverse("login"))



@login_required
def device(request, device_id):
    context = {}
    form = LogForm(request.POST or None)
    
    device = Device.objects.get(pk=device_id)
    
    context['form'] = form
    


    if form.is_valid():
        user_id = request.user.id
        created_by = Personnel.objects.get(user=user_id)

        status = form.cleaned_data['status']
        device.status =  status
        device.save()

        phone_num = form.cleaned_data['phone_num']
        address = form.cleaned_data['address']
        name = form.cleaned_data['name']
        description = form.cleaned_data['description']
        
        log = DeviceLog(device=device,address=address, name=name,created_by= created_by, phone_num= phone_num, status=status, description=description)
        log.save()

        return HttpResponseRedirect(reverse("devices:device", args=(device_id,)))

    return render(request, "devices/device.html", {
        "device": device,
        "logs" : device.logs.all(),
        "form": form
    })

@login_required
def create(request):
    context = {}
    form = CreateForm(request.POST or None)

    if form.is_valid():
        name = form.cleaned_data['name']
        model = form.cleaned_data['model']
        status = form.cleaned_data['status']
        group = form.cleaned_data['group']
        brand = form.cleaned_data['brand']
        regular_checks = form.cleaned_data['regular_checks']
        description = form.cleaned_data['description']
        user_id = request.user.id
        personnel = Personnel.objects.get(user=user_id)
        print(f"hospital :  {personnel}")
        hospital = personnel.hospital
        print(f"hospital :  {hospital.name}")
 
        device = Device(name=name, model=model, status=status,group=group,brand=brand,
                          regular_checks=regular_checks,description=description)
        device.hospital = hospital
        device.save()
        return HttpResponseRedirect(reverse("devices:index"))

    context['form'] = form
    return render(request, "devices/create.html", context)
