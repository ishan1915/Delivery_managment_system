from django.contrib import admin
from .models import User, Customer, WarehouseManager, CityManager, Porter, Order, DeliveryArea

# Register User for admin (optional, but good for assigning roles manually)
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role', 'is_staff')
    search_fields = ('username', 'email')

# Customer Admin
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'city', 'pincode')
    search_fields = ('user__username', 'city', 'pincode')

@admin.register(WarehouseManager)
class WarehouseManagerAdmin(admin.ModelAdmin):
    list_display = ('user', 'warehouse_name', 'location')
    search_fields = ('user__username', 'warehouse_name', 'location')

@admin.register(CityManager)
class CityManagerAdmin(admin.ModelAdmin):
    list_display = ('user', 'city')
    search_fields = ('user__username', 'city')

@admin.register(Porter)
class PorterAdmin(admin.ModelAdmin):
    list_display = ('user', 'assigned_area')
    search_fields = ('user__username', 'assigned_area')

@admin.register(DeliveryArea)
class DeliveryAreaAdmin(admin.ModelAdmin):
    list_display = ('pincode', 'porter')
    search_fields = ('pincode', 'porter__user__username')

# ✅ Fixed OrderAdmin
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'customer',
        'get_customer_city',
        'get_customer_pincode',
        'is_packed',
        'is_shipped',
        'received_at_city',
        'out_for_delivery',
        'is_delivered',
    )
    list_filter = ('is_packed', 'is_shipped', 'received_at_city', 'out_for_delivery', 'is_delivered')
    search_fields = ('customer__user__username', 'customer__city', 'customer__pincode')
    autocomplete_fields = ['porter', 'warehouse_manager', 'city_manager']

    def get_customer_city(self, obj):
        return obj.customer.city
    get_customer_city.short_description = 'City'

    def get_customer_pincode(self, obj):
        return obj.customer.pincode
    get_customer_pincode.short_description = 'Pincode'
