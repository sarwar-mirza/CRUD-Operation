from django.contrib import admin
from .models import Picture


# Register your models here.
@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'product_pic', 'date']
