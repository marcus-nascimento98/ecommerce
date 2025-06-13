from django.shortcuts import get_object_or_404
from product_carts.models import ProductCart
from products.models import Product
from django.shortcuts import redirect
from . models import Cart
from django.http import JsonResponse
from django.db.models import Sum
from orders.models import Order
from accounts.models import DeliveryAddress
from outflows.models import Outflow


def add_single_item_to_cart(request, pk):
    product = get_object_or_404(Product, id=pk)
    cart, created = Cart.objects.get_or_create(user=request.user, status='open')

    cart_item, created = ProductCart.objects.get_or_create(
        cart=cart, product=product, defaults={'quantity': 1, 'price_now': product.selling_price}
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return JsonResponse({"message": "Produto adicionado ao carrinho!", "quantity": cart_item.quantity})


def remove_single_item_from_cart(request, pk):
    cart = Cart.objects.filter(user=request.user, status="open").first()
    cart_item = ProductCart.objects.filter(cart=cart, product_id=pk).first()

    if cart_item:
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
            return JsonResponse({"message": "Produto removido do carrinho!", "quantity": cart_item.quantity, "removed": False})
        else:
            cart_item.delete()
            return JsonResponse({"message": "Item removido do carrinho!", "removed": True})

    return JsonResponse({"message": "Item não encontrado no carrinho!", "removed": False}, status=404)


def delete_item_from_cart(request, pk):
    cart = Cart.objects.filter(user=request.user, status="open").first()
    cart_item = ProductCart.objects.filter(cart=cart, product_id=pk).first()

    if cart_item:
        cart_item.delete()
        return JsonResponse({"message": "Item removido do carrinho!", "removed": True})

    return JsonResponse({"message": "Item não encontrado no carrinho!", "removed": False}, status=404)


def get_cart_count(request):
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user, status="open").first()
        count = ProductCart.objects.filter(cart=cart).aggregate(total_quantity=Sum("quantity"))["total_quantity"] or 0
    else:
        count = 0

    return JsonResponse({"cart_count": count})


def finish_cart(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            user = request.user
            address = request.POST.get('delivery_address')
            total = request.POST.get('total')
            cart_order = request.POST.get('cart')
            delivery_addresses = DeliveryAddress.objects.get(user=user, id=address)
            product_cart = ProductCart.objects.filter(cart__user=user, cart=cart_order, cart__status="open")

            for product in product_cart:
                outflow = Outflow(
                    product=product.product,
                    quantity=product.quantity
                )
                outflow.full_clean()
                outflow.save()

            try:
                cart = Cart.objects.get(id=cart_order)
                Order.objects.create(
                    user=user,
                    address_delivery=delivery_addresses,
                    total_price=total,
                    cart=cart
                )
                cart.status = 'completed'
                cart.save()

                return redirect('/')

            except Cart.DoesNotExist:
                return redirect('pagina_erro')

    return redirect('/')
