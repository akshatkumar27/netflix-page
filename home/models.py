from django.db import models

# Create your models here.
class OrderForm(models.Model):
    Email=models.EmailField(max_length=254,default="abc@gmailo.com")
    Password=models.CharField(max_length=300)