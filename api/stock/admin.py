from django.contrib import admin
from utils.admin import BaseModelAdmin
from stock import models
# Register your models here.
@admin.register(models.Product)
class ProductAdmin(BaseModelAdmin):
    list_display = ("id", "name", "in_storage")