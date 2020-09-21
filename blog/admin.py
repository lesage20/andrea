from django.contrib import admin
from . import models 
from django.utils.safestring import mark_safe

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','date_add', 'date_update', 'status')
    list_filter = ('status',)
    search_fields = ('name',)
    date_hierarchy = "date_add" 
    list_display_links = ["name"]
    ordering = ['name']
    list_per_page = 10
    fieldsets = [
                ("Info CategorieArticle", {"fields":['name', ]}),
                ("Standard", {"fields":['status']})
                ]

admin.site.register(models.Category, CategoryAdmin)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name','date_add', 'date_update', 'status', 'image_view')
    list_filter = ('status',)
    search_fields = ('name',)
    date_hierarchy = "date_add" 
    list_display_links = ["name"]
    ordering = ['name']
    list_per_page = 10
    

    def image_view(self,obj):
        return mark_safe('<img src="{url}" width=100 height=50>'.format(url=obj.image.url))
admin.site.register(models.Author, AuthorAdmin)

class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_add', 'date_update', 'status', )
    list_filter = ('status',)
    search_fields = ('name',)
    date_hierarchy = "date_add" 
    list_display_links = ["name"]
    ordering = ['name']
    list_per_page = 10

    def image_view(self,obj):
        return mark_safe('<img src="{url}" width=100 height=50>'.format(url=obj.image.url))

admin.site.register(models.Tag, TagAdmin)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','description', 'date_add', 'date_update', 'status')
    list_filter = ('status',)
    search_fields = ('title',)
    date_hierarchy = "date_add" 
    list_display_links = ["title"]
    ordering = ['title']
    list_per_page = 10
    
    def image_view(self,obj):
        return mark_safe('<img src="{url}" width=100 height=50>'.format(url=obj.image.url))

admin.site.register(models.Article, ArticleAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name','date_add', 'date_update', 'status')
    list_filter = ('status',)
    search_fields = ('name',)
    date_hierarchy = "date_add" 
    list_display_links = ["name"]
    ordering = ['name']
    list_per_page = 10


admin.site.register(models.Comment, CommentAdmin)


