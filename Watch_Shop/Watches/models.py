from django.db import models

# Create your models here.

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

