from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from inventory.models import Product
from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from .models import Order
from .forms import OrderCreateForm


def place_order(request, *args, **kwargs):
    if request.method == "GET":
        all_products = Product.objects.all()
        context = {
            "products": [model_to_dict(p) for p in all_products]
        }
        return render(request, "orders/place-order.html", context=context)

@api_view(("POST",))
@csrf_exempt
def api_place_order(request, *args, **kwargs):
    cart = request.data.get("cart")
    products = [Order.objects.get(name=item.item_name) for item in cart]


def get_all_orders(request, *args, **kwargs):
    if request.method =="GET":
        orders = Order.objects.all()
        context = {
            "orders": orders,
            "order_count": orders.count()
        }
        return render("orders/list.html", context=context)
    
def get_for_status(request, *args, **kwargs):
    if request.method == "GET":
        status = request.kwargs.get("status")
        status = status.to_upper()[0]
        
        orders = Order.objects.filter(status=status)
        context = {
            "orders": orders,
            "order_count": orders.count()
        }
        return render("orders/list-category.html", context=context)
        