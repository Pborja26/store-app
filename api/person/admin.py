from django.contrib import admin
from person import models
from utils.admin import BaseModelAdmin
# Register your models here.
@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "first_name", "email"]
    readonly_fields = ["last_login", "date_joined"]
    filter_horizontal = ["groups", "user_permissions"]