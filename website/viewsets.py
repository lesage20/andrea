from rest_framework import viewsets 
from rest_framework.response import Response 
from .models import * 
from .serializers import  *

class SiteInfoViewSet(viewsets.ModelViewSet):
    serializer_class = SiteInfoSerializer 
    queryset = SiteInfo.objects.all()


class AboutViewSet(viewsets.ModelViewSet):
    serializer_class = AboutSerializer 
    queryset = About.objects.all()


class ContactViewSet(viewsets.ModelViewSet):
    serializer_class = ContactSerializer 
    queryset = Contact.objects.all()


class ContactFormViewSet(viewsets.ModelViewSet):
    serializer_class = ContactFormSerializer 
    queryset = ContactForm.objects.all()

class NewsletterViewSet(viewsets.ModelViewSet):
    serializer_class = NewsletterSerializer 
    queryset = Newsletter.objects.all()



