from django.db import models
from phone_field import PhoneField
# Create your models here.

class SiteInfo(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    map_url = models.TextField()
    
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    
    

    class Meta:
        verbose_name = ("siteinfo")
        verbose_name_plural = ("siteinfos")

    def __str__(self):
        return self.name

class About(models.Model):
    image = models.ImageField(upload_to="images/about")
    description = models.TextField()
    title = models.CharField(max_length=250)
    
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    

    class Meta:
        verbose_name = ("about")
        verbose_name_plural = ("abouts")

    def __str__(self):
        return self.title


class Contact(models.Model):
    
    address = models.CharField(max_length=50)
    phone = PhoneField()
    email = models.EmailField(max_length=254)
    website = models.CharField(max_length=50)
    
    
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    

    class Meta:
        verbose_name = ("Contact")
        verbose_name_plural = ("Contacts")

    def __str__(self):
        return self.website

class ContactForm(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=50)
    message = models.TextField()
    
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    

    class Meta:
        verbose_name = ("ContactForm")
        verbose_name_plural = ("ContactForms")

    def __str__(self):
        return self.name


class Newsletter(models.Model):
    
    email = models.EmailField(max_length=254)
    
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    

    class Meta:
        verbose_name = ("Newsletter")
        verbose_name_plural = ("Newsletters")

    def __str__(self):
        return self.email

