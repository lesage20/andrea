from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    
    
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    
    

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("Category_detail", kwargs={"pk": self.pk})

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    image = models.ImageField(upload_to="images/authors")
    
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    
    

    class Meta:
        verbose_name = ("author")
        verbose_name_plural = ("authors")

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("author_detail", kwargs={"pk": self.pk})

class Tag(models.Model):
    name = models.CharField(max_length=50)
    
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    
    

    class Meta:
        verbose_name = ("Tag")
        verbose_name_plural = ("Tags")

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("Tag_detail", kwargs={"pk": self.pk})

class Article(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to="images/artciles")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="article_category")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="article_author")
    tags = models.ManyToManyField(Tag)
    slug = models.SlugField(blank=True)
    
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    
    
    

    class Meta:
        verbose_name = ("article")
        verbose_name_plural = ("articles")

    def __str__(self):
        return self.title

    
    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)
        
    def get_absolute_url(self):
        return reverse("single", kwargs={"slug": self.slug})
    

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="article_comment")
    name = models.CharField(max_length=50)
    comment = models.TextField()
    
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    
    

    class Meta:
        verbose_name = ("Comment")
        verbose_name_plural = ("Comments")

    def __str__(self):
        return self.name


