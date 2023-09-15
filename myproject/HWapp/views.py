from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django import forms
import logging
import datetime

from django.views.generic import DetailView

from HWapp.models import Client, Order, Product
from HWapp.forms import ImageForm
import datetime

from django.views.generic.dates import MonthArchiveView, WeekArchiveView, ArchiveIndexView, YearArchiveView

logger = logging.getLogger(__name__)


def index(request):
    logger.info('Index page accessed')
    return HttpResponse("<h1>Главная страница<h1>")


def about(request):
    logger.info('About page accessed')
    return HttpResponse("<h1>Страница обо мне.</h1>")


def sorted_on_date(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    return render(request, 'HWapp/sorted_on_date.html', {'client_id': client_id})


def sorted_on_week(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    orders = Order.objects.filter(client=client)
    return render(request, 'HWapp/sorted_on_week.html', {'orders': orders})


def sorted_on_month(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    orders = Order.objects.filter(client=client)
    return render(request, 'HWapp/sorted_on_month.html', {'orders': orders})


def sorted_on_year(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    orders = Order.objects.filter(client=client)
    return render(request, 'HWapp/sorted_on_year.html', {'orders': orders})


def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
    else:
        form = ImageForm()
    return render(request, 'HWapp/upload_image.html', {'form': form})

