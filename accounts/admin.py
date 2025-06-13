from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . models import CustomUser, DeliveryAddress


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('address', 'phone_number', 'city', 'state', 'zip_code', 'house_number')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('address', 'phone_number', 'city', 'state', 'zip_code', 'house_number')}),
    )


class DeliveryAddressAdmin(admin.ModelAdmin):
    list_display = ('zip_code', 'location_type', 'street_name', 'number', 'address_complement', 'reference_point', 'neighborhood', 'city', 'state', 'created_at', 'updated_at',)
    search_fields = ('city', 'state',)


admin.site.register(DeliveryAddress, DeliveryAddressAdmin)
