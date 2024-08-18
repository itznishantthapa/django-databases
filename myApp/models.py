from django.db import models

# Create your models here.
class MyAppDB(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField(max_length=4)
    address=models.TextField(max_length=20)
    phone=models.CharField(max_length=14)
    registred_at=models.DateField(auto_now_add=True)