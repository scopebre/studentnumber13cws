from django.contrib import admin
from .models import Category, Product, Order

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'stock_quantity']
    list_filter = ['category']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'quantity', 'total_price', 'customer_name','customer_email']