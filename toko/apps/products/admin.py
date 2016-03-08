from django.contrib import admin

from .models import (
    Product, Photo, ProductVariation
)


class PhotoInline(admin.StackedInline):
    model = Photo
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ('name', 'is_active', 'price', 'stock')
    inlines = [PhotoInline]

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for instance in instances:
            if not change:
                instance.created_by = request.user
            instance.save()

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        obj.save()


class ProductVariationAdmin(admin.ModelAdmin):
    model = ProductVariation
    list_display = ('name', 'is_active', 'price', 'stock')


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductVariation, ProductVariationAdmin)
