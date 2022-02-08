from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('links', views.links, name='links'),
    path('sertificates', views.sert, name='sert'),
]
