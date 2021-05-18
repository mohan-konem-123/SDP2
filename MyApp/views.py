from django.shortcuts import render, redirect
from .models import Item, cart as ct
# Create your views here.

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def cart(request):
    user = request.user
    items = ct.objects.filter(user = user.id)
    t_amount = 0
    for i in items:
        t_amount = t_amount + i.item.price
    print(t_amount)
    context = {
    'items' : items,
    't_amount' : t_amount
    }
    return render(request, 'cart.html', context)



def addToCart(request):
    id = request.POST.get('id')
    item = Item.objects.get(id=id)
    user = request.user
    c = ct(user = user, item = item)
    c.save()
    return redirect('cart')

def checkout(request):
    return render(request, 'checkout.html')

def contact(request):
    return render(request, 'contact-us.html')

def shop(request):
    items = Item.objects.all()
    return render(request, 'shop.html', {'items':items})

