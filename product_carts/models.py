from django.db import models
from carts.models import Cart
from products.models import Product


class ProductCart(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.PROTECT, related_name='carts')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='carts')
    quantity = models.IntegerField()
    price_now = models.DecimalField(max_digits=20, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Cart #{self.cart.id} - Product #{self.product.id} (Qty: {self.quantity})"
