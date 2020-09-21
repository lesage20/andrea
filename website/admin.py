from django.contrib import admin
from . import models 
from django.utils.safestring import mark_safe




class SiteInfoAdmin(admin.ModelAdmin):
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

admin.site.register(models.SiteInfo, SiteInfoAdmin)

class AboutAdmin(admin.ModelAdmin):
    list_display = ('title','date_add', 'date_update', 'status', 'image_view')
    list_filter = ('status',)
    search_fields = ('title',)
    date_hierarchy = "date_add" 
    list_display_links = ["title"]
    ordering = ['title']
    list_per_page = 10
    fieldsets = [
                ("Info CategorieArticle", {"fields":['title', 'image', 'description']}),
                ("Standard", {"fields":['status']})
                ]

    def image_view(self,obj):
        return mark_safe('<img src="{url}" width=100 height=50>'.format(url=obj.image.url))
admin.site.register(models.About, AboutAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('website','email', 'date_add', 'date_update', 'status', )
    list_filter = ('status',)
    search_fields = ('website',)
    date_hierarchy = "date_add" 
    list_display_links = ["website"]
    ordering = ['website']
    list_per_page = 10
    fieldsets = [
                ("Info CategorieArticle", {"fields":['website', 'email', 'phone' , 'address']}),
                ("Standard", {"fields":['status']})
                ]
    def image_view(self,obj):
        return mark_safe('<img src="{url}" width=100 height=50>'.format(url=obj.image.url))

admin.site.register(models.Contact, ContactAdmin)

class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('name','email', 'date_add', 'date_update', 'status')
    list_filter = ('status',)
    search_fields = ('name',)
    date_hierarchy = "date_add" 
    list_display_links = ["name"]
    ordering = ['name']
    list_per_page = 10
    fieldsets = [
                ("Info CategorieArticle", {"fields":['name', 'email', 'subject', 'message']}),
                ("Standard", {"fields":['status']})
                ]
    def image_view(self,obj):
        return mark_safe('<img src="{url}" width=100 height=50>'.format(url=obj.image.url))

admin.site.register(models.ContactForm, ContactFormAdmin)

class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email','date_add', 'date_update', 'status')
    list_filter = ('status',)
    search_fields = ('email',)
    date_hierarchy = "date_add" 
    list_display_links = ["email"]
    ordering = ['email']
    list_per_page = 10
    fieldsets = [
                ("Info CategorieArticle", {"fields":['email']}),
                ("Standard", {"fields":['status']})
                ]

admin.site.register(models.Newsletter, NewsletterAdmin)


