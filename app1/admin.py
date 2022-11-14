from django.contrib import admin
# import the UserProfile model from the models folder in app1 
from app1.models import UserProfile, Testimonial, JobCategories, PostCategory, BlogPost, Comment, CommentLike, AddService, SiteSetting, Contact

# Register your models here.
# register the UserProfile model 
admin.site.register(UserProfile)
# register the Testimonial model 
admin.site.register(Testimonial)
# reister the JobCategories model 
admin.site.register(JobCategories)
# register the PostCategory model 
admin.site.register(PostCategory)

class PostAdmin(admin.ModelAdmin):
    list_display = ('post_title', 'slug', 'status', 'created_date')
    list_filter = ('status',)
    search_fields = ['post_title', 'content']
    prepopulated_fields = {'slug': ('post_title',)}
# register the BlogPost model 
admin.site.register(BlogPost, PostAdmin)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)
# register the CommentLike model 
admin.site.register(CommentLike)
# register the AddService model 
admin.site.register(AddService)
# register the SiteSetting model 
admin.site.register(SiteSetting)
# register the Contact model 
admin.site.register(Contact)
