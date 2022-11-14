from django.db import models
from django.contrib.auth.models import User
# import timezone from django.utils
from django.utils import timezone


# Create your models here.

# The model for user is created here
class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete =models.CASCADE)
    age = models.IntegerField()
    website = models.URLField(null= True, blank = True)
    def __str__(self):
        return self.user.username

# create a model to save JobCategories
class JobCategories(models.Model):
    job_name = models.CharField(verbose_name='Job Title', max_length=100)
    description = models.TextField(verbose_name='Description', blank=True, null=True)
    def __str__(self):
        return self.job_name

# create a model to save testimonials 
class Testimonial(models.Model):
    testimonial_title = models.CharField(max_length = 150, verbose_name ='Testimonial Title')
    testimonial_name = models.CharField(max_length = 150, verbose_name = 'Testimonial Name')
    testimonial_job = models.ForeignKey(JobCategories, on_delete = models.CASCADE, verbose_name = 'Job Title', blank=True, null=True)
    testimonial_img = models.ImageField(blank = True, null = True, verbose_name = 'Testimonial Image')
    testimonial_contents = models.TextField(verbose_name = 'Testimonial Contents')
    def __str__(self):
        return self.testimonial_title

# Create a model for the post categories 
class PostCategory(models.Model):
    category_name = models.CharField(max_length = 150, verbose_name = 'Category name')
    category_description = models.TextField(verbose_name = 'Description', blank = True, null = True)
    def __str__(self):
        return self.category_name


STATUS = (
    (0, "Draft"),
    (1, "Publish")
)
# create a model to post on blog 
class BlogPost(models.Model):
    post_title = models.CharField(max_length =150, verbose_name = 'Post Title')
    slug = models.SlugField(max_length=200, unique=True, blank = True, null = True)
    post_author = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name= 'Author')
    post_category = models.ForeignKey(PostCategory, on_delete = models.CASCADE, verbose_name = 'Post Category')
    post_img = models.ImageField(blank = True, null = True, verbose_name = 'Post Featured Image')
    created_date = models.DateTimeField(default = timezone.now)
    updated_on = models.DateTimeField(auto_now=True, blank = True, null = True)
    post_contents = models.TextField(verbose_name = 'Post Contents')
    status = models.IntegerField(choices=STATUS, default=0, blank = True, null = True)
    class Meta:
        ordering  = ['-created_date']
    def __str__(self):
        return self.post_title

# create a model for comment 
class Comment(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    liked = models.ManyToManyField(User, blank=True, related_name='likes')
    created_on = models.DateTimeField(auto_now_add = True)
    active = models.BooleanField(default=False)
    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)

# create a tuple to use in the CommentLike model 
LIKE_CHOICES=(
    ('Like', 'Like'),
    ('Unlike', 'Unlike')
)
# create a model called comment like 
class CommentLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete = models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, max_length=8)
    created_on = models.DateTimeField(auto_now_add = True)
    updated_on = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return f"{self.user}-{self.comment}-{self.value}"

# create a model to add services 
class AddService(models.Model):
    service_title = models.CharField(max_length = 150, verbose_name = "Service Title")
    service_img = models.ImageField(verbose_name = "Post Service Image")
    service_contents = models.TextField(verbose_name = "Service Contents")

    def __str__(self):
        return self.service_title

# create a model for site settings 
class SiteSetting(models.Model):
    site_name = models.CharField(max_length = 150, verbose_name = "Site Name")
    site_logo = models.ImageField(verbose_name = "Site Logo", blank = True, null = True)
    site_address = models.TextField(verbose_name = "Company Address", blank = True, null = True)
    site_phone = models.CharField(max_length = 150, verbose_name = "Company Phone Number", blank = True, null = True)
    site_email1 = models.EmailField(max_length = 254, verbose_name = "Company Email", blank = True, null = True)
    site_email2 = models.EmailField(max_length = 254, verbose_name = "Customer Service Email", blank = True, null = True)
    def __str__(self):
        return self.site_name

class Contact(models.Model):
    contact_name = models.CharField(max_length =150, verbose_name ="Name")
    contact_email = models.EmailField(max_length = 150, verbose_name = "Email Address")
    contact_subject = models.CharField(max_length = 150, verbose_name = "Subject")
    contact_contents = models.TextField(verbose_name = "Contact Message")


