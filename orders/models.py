from django.db import models
from carts.models import Cart
from accounts.models import DeliveryAddress
from django.contrib.auth.models import User
from django.conf import settings


class Order(models.Model):
    STATUS_CHOICES = [
        ('paid', 'Paid'),
        ('pending', 'Pending'),
        ('sent', 'Sent'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    ]

    cart = models.ForeignKey(Cart, on_delete=models.PROTECT, related_name='orders')
    address_delivery = models.ForeignKey(DeliveryAddress, on_delete=models.PROTECT, related_name='orders', null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="orders")
    total_price = models.DecimalField(max_digits=20, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order #{self.id} - User: {self.user.username} - Status: {self.status}"
