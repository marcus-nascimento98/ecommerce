from django.shortcuts import render
from django.views.generic import ListView
from . models import ProductCart
from accounts.models import DeliveryAddress


class ProductCartListView(ListView):
    model = ProductCart
    template_name = 'products_cart.html'
    context_object_name = 'products_cart'

    def get_queryset(self):
        return ProductCart.objects.filter(cart__user=self.request.user, cart__status="open")    

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        user = self.request.user
        delivery_addresses = DeliveryAddress.objects.filter(user=user)
        context['delivery_address'] = delivery_addresses
        return context
