from django.shortcuts import render, redirect
from .models import Item, cart as ct, Bill
from .forms import BillForm
# Create your views here.

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def cart(request):
    user = request.user
    items = ct.objects.filter(user=user.id)
    t_amount = 0
    for i in items:
        t_amount = t_amount + i.item.price
    print(t_amount)
    context = {
    'items': items,
    't_amount': t_amount
    }
    return render(request, 'cart.html', context)



def addToCart(request):
    id = request.POST.get('id')
    item = Item.objects.get(id=id)
    user = request.user
    c = ct(user=user, item=item)
    c.save()
    return redirect('cart')

def checkout(request):
    user = request.user
    items = ct.objects.filter(user=user.id)
    t_amount = 0
    for i in items:
        t_amount = t_amount + i.item.price
    if request.method=='POST':
        postdata = request.POST
        firstname = postdata.get('firstname')
        lastname = postdata.get('lastname')
        username = postdata.get('username')
        email = postdata.get('email')
        address2 = postdata.get('address2')
        country = postdata.get('country')
        state = postdata.get('state')
        zip = postdata.get('zip')
        payment = postdata.get('payment')
        cardname = postdata.get('cardname')
        cardnumber = postdata.get('cardnumber')
        b = Bill(firstname=firstname, lastname=lastname, username=username, email=email, address1=address2,
                 address2=address2, country=country, state=state, zip=zip, payment=payment, cardnumber=cardnumber,
                 cardname=cardname)
        b.register()
        return redirect('/')
    else:
        form = BillForm()
        context = {
            'items': items,
            't_amount': t_amount,
            'discount': (t_amount * 5) / 100,
            'total': t_amount - (t_amount * 5) / 100
        }
        return render(request, 'checkout.html',context)

def contact(request):
    return render(request, 'contact-us.html')

def shop(request):
    items = Item.objects.all()
    return render(request, 'shop.html', {'items':items})


