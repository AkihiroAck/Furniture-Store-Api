from django.contrib import admin
from .models import Furniture, Order, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Furniture)
class FurnitureAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')
    search_fields = ('name', 'category')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer_email', 'total_price', 'created_at')
    search_fields = ('customer_email',)
    list_filter = ('created_at',)