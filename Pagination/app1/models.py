from django.db import models

# Create your models here.

class Product(models.Model):
    pid = models.IntegerField()
    pname = models.CharField(max_length=50)
    price = models.IntegerField()



    def __str__(self):
        return f"{self.pname}--{self.price}"