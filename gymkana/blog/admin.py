from django.contrib import admin
from .models import New, Event


class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'subtitle', 'publish_date']

class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'subtitle', 'start_date', 'end_date']

admin.site.register(New,NewsAdmin)
admin.site.register(Event,EventAdmin)
