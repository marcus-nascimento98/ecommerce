from django.contrib import admin
from .models import Cart


class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'status', 'created_at', 'updated_at')
    search_fields = ('user', 'status',)

admin.site.register(Cart, CartAdmin)
