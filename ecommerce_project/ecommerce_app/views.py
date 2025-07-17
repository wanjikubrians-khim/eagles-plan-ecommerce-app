from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import Product
from .cart import Cart

def index(request):
    products = Product.objects.all()
    return render(request, 'ecommerce_app/index.html', {'products': products})

def about(request):
    return render(request, 'ecommerce_app/about.html')

@csrf_exempt
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        # You can later replace this with actual email or DB saving logic
        print(f"Contact form received:\n{name}\n{email}\n{message}")
        return HttpResponse("Thanks! We'll get back to you soon.")
    return render(request, 'ecommerce_app/contact.html')

def cart_view(request):
    cart = Cart(request)
    return render(request, 'ecommerce_app/cart.html', {'cart': cart})

def add_to_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product_id)
    return redirect('cart')
