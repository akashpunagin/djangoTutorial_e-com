from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Contact,Order,OrderUpdate
from math import ceil
import json

# Create your views here.
def index(request):
    # products = Product.objects.all()
    # print(products)
    # n = len(products)
    # nSlides = n//4 + ceil((n/4)-(n//4))

    allProds = []
    catprods = Product.objects.values('category','id')
    # print(catprods)
    cats = {item['category'] for item in catprods}
    # print("cats = {}".format(cats))
    for cat in cats:
        # print("cat={}".format(cat))
        prod = Product.objects.filter(category=cat)
        # print("prod={}".format(prod))
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    print("allprods = {}".format(allProds))

    # params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'product': products}
    # allProds = [[products, range(1, nSlides), nSlides],
    #             [products, range(1, nSlides), nSlides]]
    params = {'allProds':allProds}
    return render(request, 'shop/index.html', params)

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    thank = False
    if request.method == "POST":
        # print(request)
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        desc = request.POST.get('desc','')
        contact = Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()
        thank = True
    return render(request, 'shop/contact.html',{'thank':thank})

def tracker(request):
    if request.method=="POST":
        order_id = request.POST.get('orderid', '')
        email = request.POST.get('email', '')
        try:
            order = Order.objects.filter(order_id=order_id,email=email)
            if len(order):
                update = OrderUpdate.objects.filter(order_id=order_id)
                updates = []
                for item in update:
                    updates.append({'text':item.update_desc,'time':item.timestamp})
                    response = json.dumps(updates, default=str)
                console.log(response)
            else:
                HttpResponse({})
        except Exception as e:
            HttpResponse({})
    return render(request, 'shop/tracker.html')

def search(request):
    return render(request, 'shop/search.html')

def productview(request,myid):
    # fetch product using id
    product = Product.objects.filter(id=myid)
    print(product)

    return render(request, 'shop/prodview.html',{'product':product[0]})

def checkout(request):
    if request.method=="POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
        order = Order(items_json=items_json, name=name, email=email, address=address, city=city,state=state, zip_code=zip_code, phone=phone)
        order.save()
        update = OrderUpdate(order_id=order.order_id,update_desc="The order is been placed")
        update.save();
        thank = True
        id = order.order_id
        return render(request, 'shop/checkout.html', {'thank':thank, 'id': id})
    return render(request, 'shop/checkout.html')
