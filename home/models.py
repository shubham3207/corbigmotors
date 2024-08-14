from django.db import models

# Create your models here.
class Product(models.Model):
    COLOR_CHOICES=[
        ('black', 'Black'),
        ('red', 'Red'),
         ('grey', 'Grey'),
          ('green', 'Green'),
           ('blue', 'Blue'),
            ('white', 'White'),
    ]
    name= models.CharField(max_length=200,  )
    color= models.CharField(max_length=200, choices=COLOR_CHOICES, default='red')
    price= models.FloatField(max_length=300)
    title= models.CharField(max_length=400)
    description= models.TextField(max_length=800)
    maxspeed= models.CharField(max_length=200)
    range=models.CharField(max_length=200, default=0)
    ccequivalent=models.CharField(max_length=200, default=0)

    battery= models.CharField(max_length=200,null=True, blank=True)
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
    
