from django.contrib import admin
from .models import Product, Photo, ProductVariation


class PhotoInline(admin.StackedInline):
    model = Photo
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ('name', 'is_active', 'price', 'stock')
    inlines = [PhotoInline]


class ProductVariationAdmin(admin.ModelAdmin):
    model = ProductVariation
    list_display = ('name', 'is_active', 'price', 'stock')

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductVariation, ProductVariationAdmin)

