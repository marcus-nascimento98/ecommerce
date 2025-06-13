from django.db import models
from django.core.exceptions import ValidationError
from products.models import Product


class Outflow(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='outflows')
    quantity = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def clean(self):
        if self.quantity > self.product.quantity:
            raise ValidationError("A quantidade de saída é maior do que o estoque disponível.")

    def __str__(self):
        return str(self.product)
