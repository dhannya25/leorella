from django.shortcuts import render,redirect
from . models import *
# Create your views here.
def home(request):
    return render(request,'seller/home.html')
def signup(request):
    if request.method=='POST':
        namee=request.POST['name']
        emaill=request.POST['email']
        num=request.POST['number']
        pswd=request.POST['password']
        Sell=Seller(name=namee,email=emaill,mob=num,password=pswd)
        Sell.save()
        return redirect('seller:login')
    return render(request,'seller/signup.html')
def login(request):
    if request.method=='POST':
        email=request.POST['email']
        pswd=request.POST['password']
        try:
            seller=Seller.objects.get(email=email,password=pswd)
            request.session['seller']=seller.id
            return redirect('seller:sellerdashboard')
        except Seller.DoesNotExist:
            return render(request,'seller/login.html',{'msg':'invalid username or password'})
        # if Seller.objects.filter(email=email,password=pswd).exists():
        #     return redirect('seller:sellerdashboard')
        # else:
        #     return render(request,'seller/login.html',{'msg':'invalid mail and pswd'})
    return render(request,'seller/login.html')
def sellerdashboard(request):
    if 'seller' in request.session:
        return render(request,'seller/sellerdashboard.html')
    else:
        return render(request,'seller/errorpage.html')
def addpdt(request):
    cat=Category.objects.all()
    if request.method=='POST':
        name=request.POST['name']
        price=request.POST['price']
        description=request.POST['description']
        image=request.FILES['image']
        cat=request.POST.get('cat')
        category=Category.objects.get(pk=cat)
        pdt=Product(p_name=name,p_price=price,p_image=image,category=category,p_description=description)
        pdt.save()
        return render(request,'seller/addproduct.html')
    return render(request,'seller/addproduct.html',{'cat':cat})

def viewpdt(request):
    pdts=Product.objects.all()
    return render(request,'seller/viewpdt.html',{'products':pdts})

def updatepdt(request,pid):
    pdt=Product.objects.get(id=pid)
    if request.method=='POST':
        name=request.POST['name']
        price=request.POST['price']
        description=request.POST['description']

    #update
        pdt.p_name=name
        pdt.p_price=price
        pdt.p_description=description
        pdt.save()
        return redirect('seller:viewpdt')
    return render(request,'seller/updatepdt.html',{'pdt':pdt})
                  
def deletepdt(request,pid):
    Pdt=Product.objects.get(id=pid).delete()
    return redirect('seller:viewpdt')


def logout(request):
    if 'seller' in request.session:
        del request.session['seller']
        return redirect('seller:home')
    
def category(request):
    if request.method=='POST':
        name=request.POST['name']
        description=request.POST['description']
        image=request.FILES['image']
        category=Category(c_name=name,c_image=image,c_description=description)
        category.save()
        return redirect('seller:sellerdashboard')
    return render(request,'seller/addcat.html')

def viewcat(request):
    category=Category.objects.all()
    return render(request,'seller/viewcat.html',{'category':category})

def updatecat(request,cat):
    category=Category.objects.get(id=cat)
    if request.method=='POST':
        name=request.POST['name']
        description=request.POST['description']
        category.c_name=name
        category.c_description=description
        category.save()
        return redirect('seller:viewcat')
    return render(request,'seller/updatecat.html',{'category':category})
def deletecat(request,cid):
    cat=Category.objects.get(id=cid).delete()
    return redirect('seller:viewcat')

