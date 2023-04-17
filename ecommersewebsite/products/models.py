from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class Seller(models.Model):
    name=models.CharField(max_length=200)
    phone=PhoneNumberField()
    email=models.EmailField( max_length=254)
    profile=models.TextField(blank=True)
    photo= models.ImageField( upload_to='seller/photos/')
    def __str__(self):
        return self.name

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Seller'
        verbose_name_plural =   'Sellers' 

class Product(models.Model):
    name=models.CharField( max_length=200)
    description=models.TextField(blank=True)
    price=models.IntegerField()
    seller=models.ForeignKey(Seller,on_delete=models.DO_NOTHING)
    photo= models.ImageField( upload_to='products/photos/')
    def __str__(self):
        return self.name

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Product'
        verbose_name_plural = 'Products'