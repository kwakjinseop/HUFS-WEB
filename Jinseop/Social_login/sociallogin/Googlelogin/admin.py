from django.contrib import admin
from .models import Google

# Register your models here.
@admin.register(Google)

class GoogleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'url')