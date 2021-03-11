from django.contrib import admin
from google.models import Google

# Register your models here.
@admin.register(Google)

class Google_admin(admin.ModelAdmin):
    list_display = ('id', 'title', 'url')