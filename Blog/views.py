from django.shortcuts import render, get_object_or_404
from django.http import Http404

# Create your views here.
from .models import BlogPost

def contact(request):
    print(request.POST)
    print(request.user)
    return render(request, 'Blog/form.html',{'title': 'Contact'})



def blog_post_list_view(request):
    queryset = BlogPost.objects.all()
    template_name = 'Blog/blog_post_list.html'
    context = {
        'blog_post_list': queryset,
        'title'         : 'Blog Posts'
    }
    return render(request, template_name, context)

def blog_post_details_view(request, slug):
    # queryset = BlogPost.objects.get(slug = slug)    #returns error, get() returned more than one BlogPost -- it returned 2!
    queryset = BlogPost.objects.filter(slug = slug) 
    blog_obj = None
    if queryset.count() >= 1:
        blog_obj = queryset.first()    #returns the first object with matching slug
    template_name = 'Blog/blog_post_details.html'
    context = {
        'blog_post': blog_obj
    }
    return render(request, template_name, context)


def blog_post_create_view(request):
    template_name = 'Blog/blog_post_create.html'
    context = {
        'title' : 'Create a New Blog'
    }
    return render(request, template_name, context)


def blog_post_update_view(request, slug):
    return render(request, template_name, context)


def blog_post_delete_view(request, slug):
    return render(request, template_name, context)


def blog_post_details_page_old(request, post_id):
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
