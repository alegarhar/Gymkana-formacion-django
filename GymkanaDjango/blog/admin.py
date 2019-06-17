from django.contrib import admin
from .models import Event, New

# Register your models here.


class BaseAdmin(admin.ModelAdmin):
    """
    Basic class to inherit
    """
    search_fields = ['__all__']


class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'start_date', 'end_date')


class NewAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'publish_date')


admin.site.register(Event, EventAdmin)
admin.site.register(New, NewAdmin)
