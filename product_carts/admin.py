from django.contrib import admin
from .models import ProductCart


class ProductCartAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'quantity', 'price_now', 'created_at', 'updated_at')
    search_fields = ('cart', 'product',)

admin.site.register(ProductCart, ProductCartAdmin)
