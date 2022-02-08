from django.shortcuts import render
from .models import Links, Info, Sertificate


def index(request):
    info = Info.objects.order_by('-id')
    return render(request, 'vizitka/index.html', {'info': info})


def links(request):
    links = Links.objects.order_by('-id')
    return render(request, 'vizitka/links.html', {'links': links})


def sert(request):
    sertificates = Sertificate.objects.order_by('-id')
    return render(request, 'vizitka/sertificates.html', {'sert': sertificates})