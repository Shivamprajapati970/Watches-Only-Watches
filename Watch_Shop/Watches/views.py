from django.shortcuts import render,redirect,get_object_or_404   #get_object_or_404
from django.http import HttpResponse 
from django.views import View
from django.db.models import Q
from .models import *
from .form import *
import razorpay
from django.conf import settings
from django.contrib import messages

# Create your views here.
def index(request):
    category_data=Category.objects.all()
    return render(request,"home.html",locals())

def Home(request):
    category_data=Category.objects.all()
    #for show total cart itme value in navbar
    totalitem=0
    if request.user.is_authenticated:
        totalitem=len(Cart.objects.filter(user=request.user))
    return render(request,"home.html",locals())

def AllProduct(request):
    all_data=Product.objects.all()
    #for show total cart itme value in navbar
    totalitem=0
    if request.user.is_authenticated:
        totalitem=len(Cart.objects.filter(user=request.user))
    return render(request,"allproduct.html",locals())

class CategoryView(View):
    def get(self,request,id):
        category_data=Category.objects.all()
        #Brand=Brand_name.objects.all()
        prod_data_cat=Product.objects.filter(category=id)
        #for show total cart itme value in navbar
        totalitem=0
        if request.user.is_authenticated:
            totalitem=len(Cart.objects.filter(user=request.user))
        return render(request,"category.html",locals())
        
    
# class CategoryBrand(View):
#     def get(self,request,id):
#         Brand=Brand_name.objects.all()
#         print(id)
#         prod_data_cat=Product.objects.filter(brand=id)
#         # brand=request.GET.get("brand")
#         # prod_data_cat=Product.objects.filter(category=id).value(brand)
#         return render(request,"category.html",locals())

        
class ProductDetail(View):
    def get(self,request,pk):
        product=Product.objects.get(pk=pk)
        #for show total cart itme value in navbar
        totalitem=0
        if request.user.is_authenticated:
            totalitem=len(Cart.objects.filter(user=request.user))
        return render(request,"product_details.html",locals())
    

class CustomerRegistration(View):
    def get(self,request):
        form=CustomerRegistrationForm()
        return render(request,'customerregistration.html',locals())
    
    def post(self,request):
        form=CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Congratulation Customer Register Successfully")
        else:
            messages.warning(request,"Invalid Input Data")
        return render(request,"customerregistration.html",locals())
    
class ProfileView(View):
    def get(self,request):
        form =CustomerProfileForm()
        #for show total cart itme value in navbar
        totalitem=0
        if request.user.is_authenticated:
            totalitem=len(Cart.objects.filter(user=request.user))
    
        return render(request,"profile.html",locals())
    def post(self,request):
        form=CustomerProfileForm(request.POST)
        if form.is_valid():
            user=request.user
            name=form.cleaned_data['name']
            locality=form.cleaned_data['locality']
            city=form.cleaned_data['city']
            mobile=form.cleaned_data['mobile']
            state=form.cleaned_data['state']
            pincode=form.cleaned_data['pincode']
            
            register=Customer(user=user,name=name,locality=locality,mobile=mobile,city=city,state=state,pincode=pincode)
            register.save()
            messages.success(request,"Congratulation Profile save successfully")

        else:
            messages.warning(request,"Invalid input Data")

        return render(request,"profile.html",locals())
    
def address(request):
    add = Customer.objects.filter(user=request.user)
    #for show total cart itme value in navbar
    totalitem=0
    if request.user.is_authenticated:
        totalitem=len(Cart.objects.filter(user=request.user))
    return render(request,'address.html',locals())

class UpdateAddress(View):
    def get(self,request,pk):
        add=Customer.objects.get(pk=pk)
        form=CustomerProfileForm(instance=add)     #instance is fill all data in form
        #for show total cart itme value in navbar
        totalitem=0
        if request.user.is_authenticated:
            totalitem=len(Cart.objects.filter(user=request.user))
        return render(request,"UpdateAddress.html",locals())
    def post(self,request,pk):
        form=CustomerProfileForm(request.POST)
        if form.is_valid():
            add=Customer.objects.get(pk=pk)
            add.name=form.cleaned_data['name']
            add.locality=form.cleaned_data['locality']
            add.city=form.cleaned_data['city']
            add.mobile=form.cleaned_data['mobile']
            add.state=form.cleaned_data['state']
            add.pincode=form.cleaned_data['pincode']
            
            add.save()
            messages.success(request,"Congratulation Profile Address Update successfully")

        else:
            messages.warning(request,"Invalid input Data")

        return redirect('address')
    
def deletaddress(request,pk):
    Customer.objects.get(id=pk).delete()
    return redirect('address')
    
def add_to_cart(request):
    user=request.user
    product_id=request.GET.get('prod_id')
    print(product_id)
    print(type(product_id))
    product=Product.objects.get(id=product_id)
    Cart(user=user,product=product).save()
    return redirect("showcart")

def show_cart(request):
    user=request.user
    cart=Cart.objects.filter(user=user)
    amount=0
    for p in cart:
        value = p.quantity * p.product.discounted_price
        amount = amount + value
        totalamount=amount + 60
    #for show total cart itme value in navbar
    totalitem=0
    if request.user.is_authenticated:
        totalitem=len(Cart.objects.filter(user=request.user))
    return render(request,"add_to_cart.html",locals())

def remove_item(request,id):
    Cart.objects.get(id=id).delete()
    return redirect("showcart")


def increase_quantity(request, pk):
    cart_item = get_object_or_404(Cart, id=pk,user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    
    return redirect('showcart')

def decrease_quantity(request,pk):
    cart_item = get_object_or_404(Cart, id=pk,user=request.user)
    
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    
    return redirect('showcart')

def Orders(request):
    orders_data=PlacedOrder.objects.filter(user=request.user)
    #for show total cart itme value in navbar
    totalitem=0
    if request.user.is_authenticated:
        totalitem=len(Cart.objects.filter(user=request.user))

    return render(request,'orders.html',locals())

class checkout(View):
    def get(self,request):
        user=request.user
        add=Customer.objects.filter(user=user)
        cart_item=Cart.objects.filter(user=user)
        amount=0
        for p in cart_item:
            value = p.quantity * p.product.discounted_price
            amount = amount + value
        totalamount=amount + 60
        razoramount=int(totalamount * 100)
        client=razorpay.Client(auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))
        data = {"amount": razoramount, "currency":"INR", "receipt":"order_rcptid_12"}
        payment_respose = client.order.create(data=data)
        print(payment_respose)

        order_id=payment_respose['id']
        order_status=payment_respose['status']
        if order_status == 'created':
            payment=Payment(
                user=user,
                amount=totalamount,
                razorpay_order_id=order_id,
                razorpay_payment_status=order_status
            )
            payment.save()

        #for show total cart itme value in navbar
        totalitem=0
        if request.user.is_authenticated:
            totalitem=len(Cart.objects.filter(user=request.user))
        return render(request,"checkout.html",locals())

def payment_done(request):
    order_id=request.GET.get('order_id')
    payment_id=request.GET.get('payment_id')
    cust_id=request.GET.get('cust_id')
    

    user=request.user
    customer=Customer.objects.get(id=cust_id)
    payment=Payment.objects.get(razorpay_order_id=order_id)
    payment.paid=True
    payment.razorpay_payment_id=payment_id
    payment.save()

    #to save order details in customer
    cart=Cart.objects.filter(user=user)
    for c in cart:
        PlacedOrder(user=user,customer=customer,product=c.product,quantity=c.quantity,payment=payment).save()
        c.delete()
    return redirect("orders")


def search(request):
    query=request.GET['search']
    product=Product.objects.filter(Q(name__icontains=query))
     #for show total cart itme value in navbar
    totalitem=0
    if request.user.is_authenticated:
        totalitem=len(Cart.objects.filter(user=request.user))
        
    return render(request,"search.html",locals())


    



#OjsWD6YMFOhi9G Razorpay marchent id   success@razorpay