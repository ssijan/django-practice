from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product
# Create your views here.

def index(request):

    products = Product.objects.all()
    
    item = {
        'products' : products,
    }
    return render(request,'shop/home.html', item)

def about(request):
    return render(request, 'shop/about_us.html')

def search(request):

    query = request.GET.get('search')
    if query:
        products = Product.objects.filter(product_name__icontains = query)
    else:
        products = Product.objects.all()
    
    item = {
        'products' : products,
        'query': query.capitalize()
    }
    return render(request, 'shop/search.html', item)


def cart_details(request):
    # We will store cart data in the session as a dictionary: {product_id: quantity}
    cart = request.session.get('cart', {})
    cart_items = []
    grand_total = 0

    # Fetch actual product objects from the database based on IDs in the cart
    for product_id, quantity in cart.items():
        product = Product.objects.get(id=product_id)
        total_price = product.price * quantity
        grand_total += total_price
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'total_price': total_price
        })

    return render(request, 'shop/cart.html', {
        'cart_items': cart_items,
        'grand_total': grand_total
    })


def add_to_cart(request, product_id):
    # 1. Get the cart from the session (or create empty dict if it doesn't exist)
    cart = request.session.get('cart', {})

    # 2. Add or increment the item quantity
    # We store the ID as a string because JSON session keys must be strings
    product_id_str = str(product_id)
    if product_id_str in cart:
        cart[product_id_str] += 1
    else:
        cart[product_id_str] = 1

    # 3. Save the cart back to the session
    request.session['cart'] = cart
    
    # 4. Redirect back to the page the user was on
    return redirect(f"{request.META.get('HTTP_REFERER', 'home')}#product-{product_id}")

def increase_cart(request, product_id):
    cart = request.session.get('cart', {})
    pro_id = str(product_id)

    if pro_id in cart:
        cart[pro_id] +=1
    
    request.session['cart'] = cart
    return redirect('cart')

def decrease_cart(request, product_id):
    cart = request.session.get('cart', {})
    pro_id = str(product_id)

    if pro_id in cart:
        if cart[pro_id] > 1:
            cart[pro_id] -= 1 
    
    request.session['cart'] = cart
    return redirect('cart')

def remove_cart(request, product_id):
    cart = request.session.get('cart', {})
    pro_id = str(product_id)
    
    del cart[pro_id]
    request.session['cart'] = cart
    return redirect('cart')