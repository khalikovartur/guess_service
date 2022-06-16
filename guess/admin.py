from django.contrib import admin

from .models import Item

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('number', 'color')
    list_filter = ('number', 'color')
    
