from django.db import models

# Create your models here.


def upload_to(instance,filename):
    return 'images/{filename}'.format(filename=filename)
class Customer(models.Model):
    customer_name=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    email=models.EmailField(max_length=40)
    phone_number=models.IntegerField()
    
    

    def __str__(self):
        return self.customer_name


class Product(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    product_name=models.CharField(max_length=50)
    price=models.FloatField()
    quantity=models.FloatField()
    sku=models.CharField(max_length=50,unique=True)
    product_image=models.ImageField(upload_to=upload_to,blank=True,null=True)
    created_date=models.DateField(auto_now=True)
    status=models.BooleanField(default=False)
    

    

