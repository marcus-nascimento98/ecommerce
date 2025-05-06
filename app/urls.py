from django.contrib import admin
from django.urls import path
from products.views import ProductListView, ProductDetailView
from product_carts.views import ProductCartListView
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from carts.views import add_single_item_to_cart, remove_single_item_from_cart, delete_item_from_cart, get_cart_count, finish_cart
from accounts.views import register_view, add_delivery_address
from orders.views import OrderListView, OrderDetailView


urlpatterns = [
    path('admin/', admin.site.urls),

    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('add/<int:pk>/', add_single_item_to_cart, name='add_single_item_to_cart'),
    path('remove/<int:pk>/', remove_single_item_from_cart, name='remove_single_item_from_cart'),
    path('delete/<int:pk>/', delete_item_from_cart, name='delete_item_from_cart'),
    path('cart/count/', get_cart_count, name='get_cart_count'),
    path('add_delivery_address/', add_delivery_address, name='add_delivery_address'),
    path('finish/', finish_cart, name='finish'),

    path('', ProductListView.as_view(), name='products_list'),
    path('cart/', ProductCartListView.as_view(), name='products_cart'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('register/', register_view, name='register'),
    path('orders/', OrderListView.as_view(), name='orders'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
