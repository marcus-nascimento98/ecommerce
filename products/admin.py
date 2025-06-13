from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'brand', 'category', 'serie_number', 'cost_price', 'selling_price', 'photo', 'quantity', 'created_at', 'updated_at',)
    search_fields = ('name', 'brand', 'serie_number', 'description',)


admin.site.register(Product, ProductAdmin)
