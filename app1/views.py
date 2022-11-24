from django.shortcuts import render, get_object_or_404
# import the Testimonial model from models.py in app1 
from app1.models import Testimonial, BlogPost, AddService, Comment
# import ListView and DetailView  from django.views.generic 
from django.views.generic import ListView, DetailView
# import contact form from the forms.py in the app1 
from app1.forms import ContactForm, CommentForm
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    service = AddService.objects.all()
    testimonial = Testimonial.objects.all()
    # filter by published post, created date and number of posts 
    blog = BlogPost.objects.filter(status=1).order_by('-created_date')[:2]
    return render(request, 'app1/index.html', {"testimonial": testimonial,
                                                "blog": blog, 
                                                "service": service
                                                })
def contact(request):
    if request.method == "POST":
        contactform = ContactForm(request.POST)
        if contactform.is_valid():
            contactform.save(commit=True)
            messages.success(request, "Message successfully submitted!")
            return HttpResponseRedirect('/app1/contact')
        else:
            messages.error(request, "Message not submitted!")
    else:
        contactform = ContactForm()
    return render(request, 'app1/contact.html', {"contactform": contactform})
    
def about(request):
    testimonial = Testimonial.objects.all()
    return render(request, 'app1/about.html', {"testimonial": testimonial})
def services(request):
    service = AddService.objects.all()
    return render(request, 'app1/services.html', {"service": service})
def test(request):
    blog = BlogPost.objects.all()
    return render(request, 'app1/test.html', {"blog": blog})


# the ListPost view will list out all the post 
class ListPost(ListView):
    model = BlogPost
    queryset = BlogPost.objects.filter(status=1).order_by('-created_date')
    template_name = 'app1/blog.html'
    context_object_name = 'post_list'
    
# the post_detail view will display the post based on the id of the post 
def post_detail(request, slug):
    template_name = 'app1/detail_post.html'
    post = get_object_or_404(BlogPost, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None 
    # comment posted 
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # create comment object but don't save to database yet 
            new_comment = comment_form.save(commit=False)
            # assign the current post to the comment 
            new_comment.post = post
            # save the comment to the database 
            new_comment.save()
            # sweetify.success(request, 'Comment successfully submitted!')
            messages.success(request, "Comment successfully submitted! Your comment will appear once approved.")
            return HttpResponseRedirect('/app1/post_detail/' + post.slug )
        else:
            messages.error(request, "Comment not submitted.")         
    else:
        comment_form = CommentForm()
    
    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})


# DASHBOARD VIEW
def dashboard(request):
    return render(request, 'app1/dashboard/index.html')

def base(request):
    return render(request, 'app1/dashboard/base.html')