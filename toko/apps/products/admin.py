from django.contrib import admin
from .models import Product, Photo, ProductVariation, Category, PhotoFeatured, ProductFeatured


class PhotoInline(admin.StackedInline):
    model = Photo
    extra = 0


class PhotoInlineFeatured(admin.StackedInline):
    model = PhotoFeatured
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ('name', 'is_active', 'price', 'stock')
    inlines = [PhotoInline]


class ProductFeaturedAdmin(admin.ModelAdmin):
    model = ProductFeatured
    list_display = ('name', 'is_active',)
    inlines = [PhotoInlineFeatured]


class ProductVariationAdmin(admin.ModelAdmin):
    model = ProductVariation
    list_display = ('name', 'is_active', 'price', 'stock')


class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ('name', 'slug', 'description', 'is_active')

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductVariation, ProductVariationAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductFeatured, ProductFeaturedAdmin)
