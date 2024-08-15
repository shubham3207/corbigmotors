from django.shortcuts import render, redirect

# Create your views here.
from .models import *

from django.contrib import messages




def homeview(request):
    views={}
    views['products'] =Product.objects.all()
    return render(request,"home.html",views)


def productview(request):
    views={}
    views['products'] =Product.objects.all()
    return render(request,"product.html",views)



from django.shortcuts import redirect

def contact(request):
    if request.method == 'POST':
        na = request.POST.get('name')
        em = request.POST.get('email')
        sub = request.POST.get('subject')
        mes = request.POST.get('message')
        pho = request.POST.get('phone')
        
        # Create and save the Contact instance
        Contact.objects.create(
            name=na,
            email=em,
            subject=sub,
            message=mes,
            phone=pho,
        )
        
        # Add a success message to be shown as a toast notification
        # messages.success(request, 'Your message has been sent successfully!')
        
        # Redirect to the same page to prevent resubmission on refresh
        # return redirect('contact')  # Replace 'contact' with your URL name

    return render(request, 'contact.html')

def about(request):
    return render(request,'about.html')

def search_view(request):
    if request.method == 'GET':
        search_query = request.GET.get('search_query', '')

        # Perform the search query on the Blog model
        products = Product.objects.filter(title__icontains=search_query)

        context = {
            'search_query': search_query,
            'products': products
        }
        return render(request, 'search.html', context)
    
def product_single(request,id):
    views = {}
    views['product_details'] = Product.objects.filter(id = id)
    return render(request,'product_detail.html',views)

