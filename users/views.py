from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "users/user.html")


@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))
