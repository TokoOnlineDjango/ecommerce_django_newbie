from django.contrib import admin

from .models import Category


class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ('name', 'slug', 'description', 'is_active')

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        obj.save()


admin.site.register(Category, CategoryAdmin)
