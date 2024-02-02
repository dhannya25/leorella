from django.shortcuts import render,redirect
from .models import *
from seller.models import *
# Create your views here.
def home(request):
    return render(request,'customer/home.html')

def signup(request):
    if request.method=='POST':
        namee=request.POST['name']
        emaill=request.POST['email']
        num=request.POST['number']
        pswd=request.POST['password']
        Cus=Customer(name=namee,email=emaill,mob=num,password=pswd)
        Cus.save()
    return render(request,'customer/signup.html')

def login(request):
    if request.method=='POST':
        email=request.POST['email']
        pswd=request.POST['password']
        try:
         customer=Customer.objects.get(email=email,password=pswd)
         request.session['customer']=customer.id
         return redirect('customer:dashboard')
        except Customer.DoesNotExist:
          return render(request,'customer/login.html',{'msg':'invalid username or password'})
    # if Customer.objects.filter(email=email,password=pswd).exists():
    #     return redirect('customer:dashboard')
    # else:
    #     return render(request,'customer/login.html',{'msg':'invalid email and pswd'})

    return render(request,'customer/login.html')
def dashboard(request):
    if 'customer' in request.session:
        return render(request,'customer/dashboard.html')
    else:
        return render(request,'customer/errorpage.html')








def logout(request):
    if 'customer' in request.session:
        del request.session['customer']
        return redirect('customer:home')
    
def Errorpage(request):
    return render(request,'customer/errorpage.html')
def ContactUs(request):
    if request.method=='POST':
        namee=request.POST['name']
        emaill=request.POST['email']
        msg=request.POST['yourmessage']
        Cus=Contactus(name=namee,email=emaill,yourmessage=msg,)
        Cus.save()
    return render(request,'customer/contactus.html')

def bagcategory(request):
    bag=Category.objects.get(c_name='BAG')
    pdt=Product.objects.filter(category=bag)
    return render(request,'customer/bagcategory.html',{'products':pdt})
def dresscategory(request):
    drs=Category.objects.get(c_name='DRESS')
    pdt=Product.objects.filter(category=drs)
    return render(request,'customer/dresscategory.html',{'products':pdt})

def footwearcategory(request):
    foot=Category.objects.get(c_name='FOOTWEAR')
    pdt=Product.objects.filter(category=foot)
    return render(request,'customer/footwearcategory.html',{'products':pdt})

def cart(request):
    cartitems =Cart.objects.all()
    total_price=sum(item.product.p_price*item.quantity for item in cartitems)
    total_price_per_item=[]
    grand_total=0
    for item in cartitems:
        item_total=item.product.p_price*item.quantity
        total_price_per_item.append({'item':'item_total'})
        grand_total+=item_total
    return render(request,'customer/cart.html',{'cartitems':cartitems,'grand_total':grand_total,'total_price':total_price})
def payment(request):
    return render(request,'customer/payment.html')
def add_to_cart(request,p_id):
    if request.method=='POST':
        product=Product.objects.get(id=p_id)
        cart_item,created=Cart.objects.get_or_create(product=product)
        if not created:
            cart_item.quantity+=1
            cart_item.save()
    return redirect('customer:cart')
def remove_from_cart(request,product_id):
    product=Product.objects.get(id=product_id)
    cart_item=Cart.objects.get(product=product)
    cart_item.delete()
    return redirect('customer:cart')

def wish(request):
    wish =Wishlist.objects.all()
    total_price=sum(item.product.p_price for item in wish)
    total_price_per_item=[]
    grand_total=0
    for item in wish:
        item_total=item.product.p_price
        total_price_per_item.append({'item':'item_total'})
        grand_total+=item_total
    return render(request,'customer/wishlist.html',{'wishlist':wish,'grand_total':grand_total,'total_price':total_price})

def add_wishlist(request,pid):
    if request.method=='POST':
        product=Product.objects.get(id=pid)
        wishlist,created=Wishlist.objects.get_or_create(product=product)
        if not created:
            wishlist.quantity+=1
            wishlist.save()
    return redirect('customer:wishlist')

def remove_from_wish(request,product_id):
    product=Product.objects.get(id=product_id)
    wishlist=Wishlist.objects.get(product=product)
    wishlist.delete()
    return redirect('customer:wishlist')