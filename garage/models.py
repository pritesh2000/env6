from django.db import models
from generic.models import BaseField


# Create your models here.
class Category(BaseField):
    category_name = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)

    class Meta():
        db_table="category"

    def __str__(self):
        return self.category_name    

class Subcategory(BaseField):
    subcategory_name = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta():
        db_table='subcategory'

    def __str__(self):
        return self.subcategory_name

    
class Service(BaseField):
    service_name = models.CharField(max_length=128)
    service_description = models.TextField(max_length=512)
    service_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available= models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)

    class Meta():
        db_table = 'service'

    def __str__(self):
        return self.service_name
   
"""
class Order(models.Model):
    STATUS = (
        ('pending', 'pending'),('processing', 'processing'), ('completed', 'completed')
    )
    customer = models.ForeignKey(Customer,null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product,null=True, on_delete=models.SET_NULL)
    data_created = models.DateTimeField(auto_now_add=True, null=True)
    STATUS = models.CharField(max_length=200, choices=STATUS)


    class Meta:
        db_table = 'order_details'
"""