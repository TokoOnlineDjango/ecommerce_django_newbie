from django.contrib import admin
from .models import Chart, ChartItem


class CharItemInline(admin.TabularInline):
    model = ChartItem
    extra = 0


class ChartAdmin(admin.ModelAdmin):
    inlines = [CharItemInline, ]

    class Meta:
        model = Chart

admin.site.register(Chart, ChartAdmin)
