from django.db import models

choices=[
    ('Rent','Rent'),
    ('Sale','Sale')
]
class Product(models.Model):
    name=models.CharField(max_length=50)
    type=models.CharField(max_length=50)
    width=models.IntegerField()
    length=models.IntegerField()
    number_of_rooms=models.PositiveIntegerField()
    number_of_bathrooms=models.PositiveIntegerField()
    funiture_ready=models.BooleanField(default=False)
    address=models.CharField(max_length=255)
    price=models.CharField(max_length=50)
    sale_type=models.CharField(choices=choices,max_length=5)
    coverphoto=models.ImageField(upload_to='media/'+str(name)+'/')
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __repr__(self):
        return self.name
    def __str__(self):
        return self.name
from interest.models import Interest
class Notified(models.Model):
    interested=models.ForeignKey(Interest,on_delete=models.CASCADE)
    requested_date=models.DateTimeField()
    approved=models.BooleanField(null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
