from django.shortcuts import render
from .models import Address


def index(request):
    return render(request, 'main/index.html')


def ListAddr(request):
    data = Address.objects.order_by('places')
    return render(request, 'main/about.html', {'data': data})
