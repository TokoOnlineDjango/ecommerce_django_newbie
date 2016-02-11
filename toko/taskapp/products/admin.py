from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ['title', 'active', ]

admin.site.register(Product,ProductAdmin )
