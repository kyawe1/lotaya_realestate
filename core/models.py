from django.db import models

choices=[
    ('Rent','Rent'),
    ('Sale','Sale')
]
class Product(models.Model):
    name=models.CharField(max_length=50)
    type=models.CharField(max_length=50)
    width=models.IntegerField(blank=True,null=True)
    length=models.IntegerField(blank=True,null=True)
    number_of_rooms=models.PositiveIntegerField()
    number_of_bathrooms=models.PositiveIntegerField()
    funiture_ready=models.BooleanField(default=False)
    address=models.CharField(max_length=255)
    price=models.CharField(max_length=50)
    sale_type=models.CharField(choices=choices,max_length=5)
    # slug=models.CharField(max_length=53)
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __repr__(self):
        return self.name
    def __str__(self):
        return self.name
    def get_upload_name(self,filename):
        return self.name+'/'+filename
    coverphoto=models.ImageField(upload_to=get_upload_name)


    def set_slug(self):
        self.slug = self.name.replace(' ','_')

   


    def is_interested(self,user):
        return True if self.interested.get(owner=user) else False
        

from interest.models import Interest


class Notified(models.Model):
    interested=models.ForeignKey(Interest,on_delete=models.CASCADE)
    requested_date=models.DateTimeField()
    approved=models.BooleanField(null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
