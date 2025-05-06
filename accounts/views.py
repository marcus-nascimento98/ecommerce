from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import CreateView
from django.shortcuts import render, redirect
from . forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.shortcuts import redirect
from . models import DeliveryAddress


def register_view(request):
    if request.method == "POST":
        user_form = CustomUserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('login')
    else:
        user_form = CustomUserCreationForm()
    return render(request, 'register.html', {'user_form': user_form})


def add_delivery_address(request):
    if request.method == 'POST':

        zip_code = request.POST.get('zip_code')
        street_name = request.POST.get('street_name')
        number = request.POST.get('number')
        neighborhood = request.POST.get('neighborhood')
        city = request.POST.get('city')
        reference_point = request.POST.get('reference_point')
        state = request.POST.get('state')
        location_type = request.POST.get('location_type')
        address_complement = request.POST.get('address_complement')
        

        if not all([zip_code, street_name, number, neighborhood, city, reference_point, state, location_type, address_complement]):
            return JsonResponse({'error': 'Campos obrigatórios faltando'}, status=400)

        DeliveryAddress.objects.create(
            user=request.user,
            zip_code=zip_code,
            address_complement=address_complement,
            street_name=street_name,
            number=number,
            neighborhood=neighborhood,
            city=city,
            reference_point=reference_point,
            state=state, 
            location_type=location_type
        )

        return redirect(request.META.get('HTTP_REFERER', '/'))

    return JsonResponse({'error': 'Método não permitido'}, status=405)


""" def add_single_item_to_cart(request, pk):
    product = get_object_or_404(Product, id=pk)
    cart, created = Cart.objects.get_or_create(user=request.user, status='open')

    cart_item, created = ProductCart.objects.get_or_create(
        cart=cart, product=product, defaults={'quantity': 1, 'price_now': product.selling_price}
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return JsonResponse({"message": "Produto adicionado ao carrinho!", "quantity": cart_item.quantity}) """
