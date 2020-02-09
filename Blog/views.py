from django.shortcuts import render

from .models import BlogPost

# Create your views here.


def blog_post_details_page(request, post_id):
    blog_obj = BlogPost.objects.get(id=post_id)
    template_name = 'Blog/blog_post_details.html'
    context = {
        'blog_post': blog_obj
    }
    return render(request, template_name, context)
