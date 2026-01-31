from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, default='')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    desc = models.TextField()
    pub_date = models.DateField()
    image = models.ImageField(upload_to='shop/images', default='')

    
    def __str__(self):
        return self.product_name

