from django.db import models

# Create your models here.
class Picture(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    product_pic = models.ImageField(upload_to='productImage')
    date = models.DateTimeField(auto_now_add=True)
