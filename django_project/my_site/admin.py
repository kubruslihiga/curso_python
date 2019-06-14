from django.contrib import admin
from .models import URLCoder


# Register your models here.
class UrlCoderAdmin(admin.ModelAdmin):
    list_display = ["url"]


admin.site.register(URLCoder, UrlCoderAdmin)
