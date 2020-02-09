from django.shortcuts import render

from .models import BlogPost

# Create your views here.
blog_obj = BlogPost.objects.get(id=1)


def blog_post_details_page(request):
    template_name = 'Blog/blog_post_details.html'
    context = {
        'blog_post': blog_obj
    }
    return render(request, template_name, context)
