from django.shortcuts import render

# Create your views here.

def fashion(request): 
    
    return render(request, "fashion.html")

def travel(request): 
    
    return render(request, "travel.html")

def single(request): 
    
    return render(request, "single.html")

