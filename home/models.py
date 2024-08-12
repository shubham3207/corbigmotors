from django.db import models

# Create your models here.
class Product(models.Model):
    name= models.CharField(max_length=200 )
    color= models.CharField(max_length=200)
    price= models.FloatField(max_length=300)
    title= models.CharField(max_length=400)
    description= models.TextField(max_length=800)
    maxspeed= models.IntegerField()
    battery: models.IntegerField()
    image1=models.ImageField(null=True, blank=True,upload_to="media")
    image2=models.ImageField(null=True, blank=True,upload_to="media")
    image3=models.ImageField(null=True, blank=True,upload_to="media")

    def __str__(self):
        return self.name

class Contact(models.Model):
    name=models.CharField(max_length=200)
    email= models.EmailField(max_length=500)
    phone= models.CharField(max_length=300)
    
    subject= models.CharField(max_length=300)
    message= models.TextField(max_length=800)

    def __str__(self):
        return self.name
    
