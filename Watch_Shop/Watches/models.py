from django.db import models
from django.contrib.auth.models import User

# Create your models here.
STATE_CHOICE=(
    ('Madhya Pradesh','Madhya Pradesh'),
    ('Uttar Pradesh','Uttar Pradesh'),
    ('Andhra Pradesh','Andhra Pradesh'),
    ('Bihar','Bihar'),
    ('Gujrat','Gujrat'),
    ('Delhi','Delhi'),
    ('Goa','Goa'),
    ('Haryana','Haryana'),
    ('Rajasthan','Rajasthan'),
    ('Maharashtra','Maharashtra'),
    
)

class Category(models.Model):
    category_name=models.CharField(max_length=50)
    cat_img=models.ImageField(upload_to="category_img")

    def __str__(self):
        return self.category_name
    
class Brand_name(models.Model):
    brand_name=models.CharField(max_length=50)
    
    def __str__(self):
        return self.brand_name
    
class Product(models.Model):
    name=models.CharField(max_length=300)
    selling_price=models.FloatField()
    discounted_price=models.FloatField()
    description=models.TextField()
    date_createtime=models.DateField(auto_now_add=True)
    date_updatetime=models.DateField(auto_now=True)
    image=models.ImageField(upload_to="Prodect_img")
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    brand=models.ForeignKey(Brand_name, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=300)
    locality=models.CharField(max_length=300)
    city=models.CharField(max_length=100)
    mobile=models.IntegerField(default=0)
    pincode=models.IntegerField()
    state=models.CharField(choices=STATE_CHOICE,max_length=200)

    def __str__(self):
        return self.name
    

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveBigIntegerField(default=1)

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price