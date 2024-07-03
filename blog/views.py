from django.shortcuts import render # type: ignore
from .models import BlogPost

def index(request):
    blogs = BlogPost.objects.all()
    return render(request, 'blog/index.html', {'blogs': blogs})
