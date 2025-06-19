# properties/models.py
from django.db import models
from django.utils import timezone




class Image(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    detail = models.TextField(default="No details available")
    image = models.ImageField(upload_to='images/')

    
  
   

    def __str__(self):
        return self.title



class Products(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    image = models.ImageField(upload_to='products/')


    def __str__(self):
        return self.title
    


class Gallery(models.Model):  
    image = models.ImageField(upload_to='gallery/')
    # created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image.name
    
    


class ImageDetail(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='details')
    title = models.CharField(max_length=100)
    detail_image = models.ImageField(upload_to='detail_images/',null=True)

    def __str__(self):
        return self.title
    

class Subscriber(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email
    

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)




class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)  # e.g., 'CEO', 'Customer'
    message = models.TextField()
    image = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.title}"
