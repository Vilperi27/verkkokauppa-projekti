from django.db import models

# Create your models here.
class Tuote(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=150)
    product_description = models.CharField(max_length=1000)
    product_image = models.CharField(max_length=2000)
    product_price = models.DecimalField(max_digits=65, decimal_places=2, default=0)

    