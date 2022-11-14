from django.urls import path
from app1 import views

app_name = 'app1'

urlpatterns = [
    path('contact/', views.contact, name = 'contact'),
    path('about/', views.about, name = 'about'),
    path('services/', views.services, name = 'services'),
    # <int:pk> will fetch the post with the primary key 
    path('post_detail/<slug:slug>', views.post_detail, name = 'post_detail'),
    path('blog/', views.ListPost.as_view(), name = 'blog'),
    path('test/', views.test, name = 'test'),
    path('dashboard/', views.dashboard, name = 'dashboard'),
    path('base/', views.base, name = 'base')
]