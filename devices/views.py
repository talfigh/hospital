from django.shortcuts import render
from devices.models import Device, DeviceLog, DeviceName, ModelName
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from users.models import Personnel
from django.contrib import messages
from hospital.models import Hospital
from django.contrib.auth.models import User
from datetime import datetime, timedelta
# from django.db.models import Q


from devices.forms import CreateForm, LogForm


# Create your views here.
# @login_require
@login_required
def index(request):
    if request.user.is_authenticated:
        query = request.GET.get('q', '')

        user_id = request.user.id
        personnel = Personnel.objects.filter(user=user_id).first()
        hospital = personnel.hospital

        if query:
            results = Device.objects.filter(name__icontains=query).distinct()

        else:
            results = Device.objects.filter(hospital=hospital)

        return render(request, 'devices/index.html', {"devices": results, "search_input": query})
    else:
        return HttpResponseRedirect(reverse("login"))


@login_required
def wait_to_check(request):
    if request.user.is_authenticated:

        results = Device.objects.filter(next_check_at__lt=datetime.today()).distinct()

        return render(request, 'devices/wait_to_check.html', {"devices": results})
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
        device.status = status
        device.save()

        phone_num = form.cleaned_data['phone_num']
        address = form.cleaned_data['address']
        name = form.cleaned_data['name']
        description = form.cleaned_data['description']

        if device.status_id == 3:
            d = datetime.today()
            d += timedelta(days=device.regular_checks * 30)
            device.next_check_at = d
            device.save()

        log = DeviceLog(device=device, address=address, name=name, created_by=created_by, phone_num=phone_num,
                        status=status, description=description)
        log.save()

        return HttpResponseRedirect(reverse("devices:device", args=(device_id,)))

    return render(request, "devices/device.html", {
        "device": device,
        "logs": device.logs.all(),
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
        next_check_at = form.cleaned_data['next_check_at_en']
        description = form.cleaned_data['description']
        user_id = request.user.id
        personnel = Personnel.objects.get(user=user_id)
        print(f"hospital :  {personnel}")
        hospital = personnel.hospital
        print(f"hospital :  {hospital.name}")

        device = Device(name=name, model=model, status=status, group=group, brand=brand,
                        regular_checks=regular_checks, description=description, next_check_at=next_check_at)
        device.hospital = hospital
        device.save()
        return HttpResponseRedirect(reverse("devices:index"))

    context['form'] = form
    return render(request, "devices/create.html", context)


@login_required
def edit(request, device_id):
    context = {}
    form = CreateForm(request.POST or None)
    device = Device.objects.filter(id=device_id).get()
    if device:
        if request.method == "POST":
            if form.is_valid():
                device.name = form.cleaned_data['name']
                device.model = form.cleaned_data['model']
                device.status = form.cleaned_data['status']
                device.group = form.cleaned_data['group']
                device.brand = form.cleaned_data['brand']
                device.regular_checks = form.cleaned_data['regular_checks']
                device.next_check_at = form.cleaned_data['next_check_at_en']
                device.description = form.cleaned_data['description']
                device.save()
                return HttpResponseRedirect(reverse("devices:index"))
        else:
            form.initial["name"] = device.name
            form.initial["model"] = device.model
            form.initial["status"] = device.status
            form.initial["group"] = device.group
            form.initial["brand"] = device.brand
            form.initial["regular_checks"] = device.regular_checks
            form.initial["next_check_at"] = device.next_check_at
            form.initial["description"] = device.description
    else:
        messages.error(request, "خطا در درخواست")
    return render(request, "devices/edit.html", {"form": form, "edit": True, "device_id": device_id})

