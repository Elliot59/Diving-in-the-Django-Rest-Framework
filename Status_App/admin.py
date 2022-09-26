from django.contrib import admin
from .models import *
# Register your models here.
class StatusAdmin(admin.ModelAdmin):
    list_display = ['user', 'id', 'content', 'image']
    class Meta:
        model = Status


admin.site.register(Status, StatusAdmin)