from django.shortcuts import render
from .models import Device, DeviceName, ModelName
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
# from django.db.models import Q


from .forms import CreateForm


# Create your views here.
@login_required
def index(request):
    query = request.GET.get('q', '')

    if query:
        # queryset = (Q(text__icontains=query))
        results = Device.objects.filter(name__icontains=query).distinct()

    else:
        results = Device.objects.all()
    return render(request, 'devices/index.html', {"devices": results, "search_input": query})


#            return render(request, "devices/index.html", {
#        "devices": Device.objects.all()
#    })

@login_required
def device(request, device_id):
    device = Device.objects.get(pk=device_id)
    return render(request, "devices/device.html", {
        "device": device
    })


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
        device = Device(name=name, model=model, status=status,group=group,brand=brand,
                          regular_checks=regular_checks,description=description)
        device.save()
        return HttpResponseRedirect(reverse("devices:index"))

    context['form'] = form
    return render(request, "devices/create.html", context)
