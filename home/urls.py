from django.urls import path
from .views import *
from . import views
urlpatterns = [
path('',homeview,name='home'),
path('product',productview,name='product'),
# path('blog_single/<int:id>', blog_single, name='blog_single'),
path('about',about,name='about'),
path('contact',contact,name='contact'),
]