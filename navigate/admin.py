from django.contrib import admin
from .models import Item

class ItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price']
    list_display_link = ['id', 'name']

admin.site.register(Item, ItemAdmin)
