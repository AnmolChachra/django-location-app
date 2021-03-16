from django.urls import path
from django.contrib import admin
from django.shortcuts import render

from .models import *
from .forms import *

admin.site.register(Place)
admin.site.register(AdministrativeArea)
admin.site.register(Locality)
admin.site.register(Country)