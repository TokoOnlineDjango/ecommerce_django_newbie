from django.contrib import admin

from .models import Category


class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ('name', 'slug', 'description', 'is_active')


admin.site.register(Category, CategoryAdmin)
