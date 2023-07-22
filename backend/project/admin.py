from django.contrib import admin
from .models import *
from django.contrib.auth.models import User
# Register your models here.
class DataAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'input_value',)

admin.site.register(Data, DataAdmin)