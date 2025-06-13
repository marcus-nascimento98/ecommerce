from django.views.generic import DetailView, ListView
from . models import Order
from product_carts.models import ProductCart


class OrderListView(ListView):
    model = Order
    template_name = 'orders.html'
    context_object_name = 'orders'


class OrderDetailView(DetailView):
    model = Order
    template_name = 'order_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        order = self.get_object()
        context['products'] = ProductCart.objects.filter(cart=order.cart)
        return context
