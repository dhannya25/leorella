from django.db import models

# Create your models here.
class Seller(models.Model):
    name=models.TextField(max_length=100,null=True)
    email=models.TextField(max_length=100,null=True)
    mob=models.PositiveIntegerField(null=True)
    password=models.TextField(max_length=100,null=True)
    
    def __str__(self):
        return self.name

    class Meta:
        db_table='seller'
class Category(models.Model):
    c_name=models.TextField(max_length=50,null=True,db_column='name')
    c_image=models.ImageField(upload_to='category',null=True,db_column="image")
    c_description=models.TextField(max_length=200,null=True,db_column='description')
    def __str__(self):
        return self.c_name
    class Meta:
        db_table='category'
    
class Product(models.Model):
    p_name=models.TextField(max_length=50,null=True,db_column='name')
    p_image=models.ImageField(upload_to='produts',null=True,db_column="image")
    p_price=models.PositiveIntegerField(null=True,db_column='price')
    p_description=models.TextField(max_length=200,null=True,db_column='description')
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.p_name
    class Meta:
        db_table='product'

