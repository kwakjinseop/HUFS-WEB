from django.contrib import admin
from .models import GoogleLogin

# Register your models here.
@admin.register(GoogleLogin)

class GoogleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'url')