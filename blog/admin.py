from django.contrib import admin # type: ignore
from .models import BlogPost

admin.site.register(BlogPost)
