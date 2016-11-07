from django.contrib import admin

# Register your models here.
from .models import ShortURL

admin.site.register(ShortURL)
