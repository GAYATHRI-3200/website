from django.shortcuts import render

# Create your views here.
def ecommerce(request):
    return render(request, 'ecommerce/ecommerce.html')

def ecommerce_single(request):
    return render(request, 'ecommerce/ecommerce-single.html')

def ecommerce_cart(request):
    return render(request, 'ecommerce/ecommerce-cart.html')        