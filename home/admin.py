from django.contrib import admin
from .models import Product, Address

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'actual_price', 'discount', 'excat_price', 'discount_cut_price', 'product_type', 'product_capacity')
    search_fields = ('name', 'product_type')
    list_filter = ('product_type',)
    ordering = ('name',)

class AddressAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'mobile_number', 'pincode', 'city', 'state', 'house_no', 'road_name', 'product')
    search_fields = ('full_name', 'city', 'state')
    list_filter = ('state',)
    ordering = ('-created_at',)  # Sort by created_at in descending order

# Register models
admin.site.register(Product, ProductAdmin)
admin.site.register(Address, AddressAdmin)

