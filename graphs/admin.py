from django.contrib import admin

from .models import Chart


class ChartAdmin(admin.ModelAdmin):
    list_display = ['title', 'order']
    list_editable = ['order',]


admin.site.register(Chart, ChartAdmin)
