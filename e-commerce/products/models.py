from django.db import models

class Products_details(models.Model):
        product_id = models.IntegerField()
        product_name = models.CharField(max_length=50)
        product_price = models.IntegerField()
        product_description = models.TextField(max_length=1000)