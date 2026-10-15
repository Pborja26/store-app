from django.db import models
from utils.models import BaseAuditModel
# Create your models here.
class Tags(BaseAuditModel):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()

class Product(BaseAuditModel):
    name = models.CharField(max_length=120, unique=True)
    description = models.TextField()
    in_storage = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    tags = models.ManyToManyField(Tags, through="ProductTags", related_name="products")

class ProductTags(BaseAuditModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tags, on_delete=models.CASCADE)




