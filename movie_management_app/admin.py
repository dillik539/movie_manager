from django.contrib import admin
from .models import WatchList, WatchedList

# Register your models here.

admin.site.register(WatchList)

admin.site.register(WatchedList)
