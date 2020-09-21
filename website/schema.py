import graphene
from graphene_django import DjangoObjectType
from . import models

class   SiteInfoType(DjangoObjectType):
    class Meta:
        model = models.SiteInfo
        fields = '__all__'

class   AboutType(DjangoObjectType):
    class Meta:
        model = models.About
        fields = '__all__'

class   ContactType(DjangoObjectType):
    class Meta:
        model = models.Contact
        fields = '__all__'
class   ContactFormType(DjangoObjectType):
    class Meta:
        model = models.ContactForm
        fields = '__all__'

class   NewsletterType(DjangoObjectType):
    class Meta:
        model = models.Newsletter
        fields = '__all__'



class Query(graphene.ObjectType):
    all_newsletters = graphene.List(NewsletterType)
    all_contact_forms = graphene.List(ContactFormType)
    all_contacts = graphene.List(ContactType)
    all_abouts = graphene.List(AboutType)
    all_site_info = graphene.List(SiteInfoType)
    
    def resolve_all_newsletters(root, info):
        return models.Newsletter.objects.all()
    
    def resolve_all_contact_forms(root, info):
        return models.Article.objects.all()
    
    def resolve_all_contacts(root, info):
        return models.Tag.objects.all()
    
    def resolve_all_abouts(root, info):
        return models.Author.objects.all()
    
    def resolve_all_site_info(root, info, name):
        return models.Category.objects.get(name=name)
        


