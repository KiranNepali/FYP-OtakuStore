from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

from carts.models import CartItem
from .models import Order, Payment
from .forms import OrderForm
import requests

import json
from django.db.models import Q


# Create your views here.


def place_order(request, total=0, quantity=0,):
    current_user = request.user
    # if the cart item is 0 redirectto store page
    cart_items = CartItem.objects.filter(user=current_user)
    cart_count = cart_items.count()
    if cart_count <= 0:
        return redirect("store")

    grand_total = 0
    tax = 0
    for cart_item in cart_items:
        total += (cart_item.product.price * cart_item.quantity)
        quantity += cart_item.quantity
    tax = (1 * total)/100
    grand_total = total + tax

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            # store billing information inside table
            data = Order()
            data.user = current_user
            data.first_name = form.cleaned_data['first_name']
            data.last_name = form.cleaned_data['last_name']
            data.phone = form.cleaned_data['phone']
            data.email = form.cleaned_data['email']
            data.address = form.cleaned_data['address']
            data.city = form.cleaned_data['city']
            data.order_note = form.cleaned_data['order_note']
            data.order_total = grand_total
            data.tax = tax
            data.save()
        context = {
            'total': total,
            'quantity': quantity,
            'cart_items': cart_items,
            'grand_total': grand_total,
            'tax': tax,
        }
        return render(request, 'orders/payments.html', context)

    else:
        return HttpResponse("hello")


def payments(request):
    payment_method = "khalti"
    token = request.GET.get("token")
    amount = request.GET.get("amount")
    print(token, amount)

    # for Verifying :

    url = "https://khalti.com/api/v2/payment/verify/"

    payload = {
        'token': token,
        'amount': amount
    }

    headers = {
        'Authorization': 'Key test_secret_key_e614eb3b75e74acd911656189794d093'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    resp_dict = response.json()
    print(resp_dict)
    data = {
        "success": True
    }

    payment = Payment(
        payment_id=token,
        user=request.user,
        amount_paid=amount,
        payment_method=payment_method,
    )
    payment.save()

    return JsonResponse(data)
