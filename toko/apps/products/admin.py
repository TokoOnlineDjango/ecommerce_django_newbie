from django.contrib import admin
from .models import Product, Photo


class PhotoInline(admin.StackedInline):
    model = Photo
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ('name', 'is_active', 'price', 'stock')
    inlines = [PhotoInline]

admin.site.register(Product, ProductAdmin)
