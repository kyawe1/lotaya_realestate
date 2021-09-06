from core.models import Product
from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class Interest (models.Model):
    owner=models.ForeignKey(get_user_model(),related_name='interested',on_delete=models.CASCADE)
    product=models.ForeignKey(Product,related_name='interested',on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    class Meta:
        unique_together=('owner','product')