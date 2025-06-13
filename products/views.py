from django.views.generic import DetailView, ListView
from .models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'products.html'
    context_object_name = 'products'

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.GET.get('category')

        if category:
            queryset = queryset.filter(category__name__icontains=category)

        return queryset


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
