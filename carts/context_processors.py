from . models import Cart
from django.db.models import Sum
from product_carts.models import ProductCart


def cart_count(request):
    user = request.user

    if user.is_authenticated:
        cart = Cart.objects.filter(user=request.user, status='open').first()
        count = ProductCart.objects.filter(cart=cart).aggregate(total_quantity=Sum("quantity"))["total_quantity"] or 0
    else:
        count = 0

    return {'cart_count': count}
