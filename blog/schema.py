import graphene
from graphene_django import DjangoObjectType
from . import models

class   CategoryType(DjangoObjectType):
    class Meta:
        model = models.Category
        fields = '__all__'

class   AuthorType(DjangoObjectType):
    class Meta:
        model = models.Author
        fields = '__all__'

class   TagType(DjangoObjectType):
    class Meta:
        model = models.Tag
        fields = '__all__'
class   ArticleType(DjangoObjectType):
    class Meta:
        model = models.Article
        fields = '__all__'

class   CommentType(DjangoObjectType):
    class Meta:
        model = models.Comment
        fields = '__all__'



class Query(graphene.ObjectType):
    all_comments = graphene.List(CommentType)
    all_articles = graphene.List(ArticleType)
    all_tags = graphene.List(TagType)
    all_authors = graphene.List(AuthorType)
    category_by_name = graphene.List(CategoryType)
    
    def resolve_all_comments(root, info):
        return models.Comment.objects.all()
    def resolve_all_articles(root, info):
        return models.Article.objects.all()
    def resolve_all_tags(root, info):
        return models.Tag.objects.all()
    def resolve_all_authors(root, info):
        return models.Author.objects.all()
    
    def resolve_category_by_name(root, info):

        return models.Category.objects.all()
        


