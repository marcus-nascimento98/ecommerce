from django.contrib import admin
from .models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ('address_delivery_id', 'user_id', 'cart', 'status', 'user', 'total_price', 'created_at', 'updated_at')
    search_fields = ('cart', 'status',)


admin.site.register(Order, OrderAdmin)
