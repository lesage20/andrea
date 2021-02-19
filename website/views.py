from django.shortcuts import render
from blog.models import *
# Create your views here.

def index(request):
    articles = Article.objects.all()
    categories = Category.objects.all()
    
    datas = {
        'articles': articles,
        'categories': categories
    }
    return render(request, "index.html", datas)

def contact(request):
    
    return render(request, "contact.html")

def about(request):
    
    return render(request, "about.html")

