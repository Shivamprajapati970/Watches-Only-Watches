from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import *
from .form import *
from django.contrib import messages

# Create your views here.
def index(request):
    category_data=Category.objects.all()
    return render(request,"home.html",locals())

def Home(request):
    category_data=Category.objects.all()
    return render(request,"home.html",locals())

def AllProduct(request):
    all_data=Product.objects.all()
    return render(request,"allproduct.html",locals())

class CategoryView(View):
    def get(self,request,id):
        category_data=Category.objects.all()
        #Brand=Brand_name.objects.all()
        prod_data_cat=Product.objects.filter(category=id)
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