# Django
from django.contrib import admin

# Local
from .models import Category

class CatagoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    list_filter = ['slug']
    search_fields = ['slug', 'title']
    ordering = ['title']
    readonly_fields = ['slug', 'created', 'modified']


admin.site.register(Category, CatagoryAdmin)
