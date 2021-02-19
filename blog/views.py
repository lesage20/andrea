from django.shortcuts import render
from  .models import *
from blog.models import *
# Create your views here.

def fashion(request): 
    articles = Article.objects.all()
    categories = Category.objects.all()
    
    datas = {
        'articles': articles,
        'categories': categories
    }
    
    
    return render(request, "fashion.html", datas)

def travel(request): 
    articles = Article.objects.all()
    categories = Category.objects.all()
    
    datas = {
        'articles': articles,
        'categories': categories
    }
    
    return render(request, "travel.html", datas)

def single(request, slug): 
    articles = Article.objects.get(slug=slug)
    
    
    datas = {
        'articles': articles,
    }
    
    return render(request, "single.html")

