from django.contrib import admin
from .models import Product,ProductVariation, ProductImage

class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ['title', 'active', ]

class ProductVariationAdmin(admin.ModelAdmin):
    model = ProductVariation
    list_display = ['title', 'active','stock','prices','product' ]

class PhotoAdmin(admin.ModelAdmin):
    model = ProductImage
    list_display = ['image','product']
    readonly_fields = ('image',)


    def image_img(self):
        if self.image:
            return u'<img src="%s" />' % self.image.url
        else:
            return '(No image found)'
        image_img.short_description = 'Thumb'
        image_img.allow_tags = True

admin.site.register(Product,ProductAdmin)
admin.site.register(ProductVariation,ProductVariationAdmin)
admin.site.register(ProductImage,PhotoAdmin)
