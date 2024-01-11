from django.shortcuts import render
from .models import BlogPost



# Create your views here.
def home(request):
    blogs = BlogPost.objects.all().filter(published = True)[:3]
    return render(request, "home/home.html", {'blogs': blogs})

def about(request):
    return render(request, 'about/about.html')
