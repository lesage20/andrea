from rest_framework import viewsets 
from rest_framework.response import Response 
from .models import * 
from .serializers import  *

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer 
    queryset = Category.objects.all()


class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer 
    queryset = Author.objects.all()


class TagViewSet(viewsets.ModelViewSet):
    serializer_class = TagSerializer 
    queryset = Tag.objects.all()


class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer 
    queryset = Article.objects.all()

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer 
    queryset = Comment.objects.all()



