from django.contrib import admin

# Register your models here.

# searchapp/admin.py

from django.contrib import admin
from .models import Dish

admin.site.register(Dish)
