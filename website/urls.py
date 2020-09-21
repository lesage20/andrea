from . import views 
from .viewsets import *
from django.urls import path, include 

from rest_framework.routers import DefaultRouter 

router = DefaultRouter()
router.register('siteinfo', SiteInfoViewSet)
router.register('about', AboutViewSet)
router.register('contact', ContactViewSet)
router.register('contactform', ContactFormViewSet)
router.register('newsletter', NewsletterViewSet)

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    
]



urlpatterns += router.urls 



