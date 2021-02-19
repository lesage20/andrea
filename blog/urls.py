from . import views 
from .viewsets import *
from django.urls import path, include 

from rest_framework.routers import DefaultRouter 

router = DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('authors', AuthorViewSet)
router.register('tag', TagViewSet)
router.register('articles', ArticleViewSet)
router.register('comments', CommentViewSet)

urlpatterns = [
    path('fashion', views.fashion, name='fashion'),
    path('travel', views.travel, name='travel'),
    path('single/<slug:slug>', views.single, name='single'),
    
]

urlpatterns += router.urls 



