from django.contrib import admin
from .models import Category, Subcategory, Service

# Register your models here.

admin.site.register(Category)

@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ['subcategory_name', 'category']
    list_filter = ['category',]
    search_fields = ['category', 'subcategory']

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['service_name', 'category', 'subcategory']
    list_filter = ['category', 'subcategory']
    search_fields = ['category', 'subcategory', 'service_name']
