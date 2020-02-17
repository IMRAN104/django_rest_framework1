from django.shortcuts import render, get_object_or_404
from django.http import Http404

# Create your views here.
from .models import BlogPost


def blog_post_details_page(request, post_id):
    print("Class of post id is: ", {post_id.__class__})

    blog_obj = get_object_or_404(BlogPost, id=post_id)
    #Broad Way of doing the same as above line
    # try:
    #     blog_obj = BlogPost.objects.get(id=post_id)
    # except BlogPost.DoesNotExist:
    #     raise Http404
    # except ValueError:
    #     raise Http404

    template_name = 'Blog/blog_post_details.html'
    context = {
        'blog_post': blog_obj
    }
    return render(request, template_name, context)
