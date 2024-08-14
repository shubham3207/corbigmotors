from django.urls import path
from .views import *
from . import views
urlpatterns = [
path('',homeview,name='home'),
path('product',productview,name='product'),
path('product_single/<int:id>', product_single, name='product_single'),
path('about',about,name='about'),
path('contact',contact,name='contact'),


]