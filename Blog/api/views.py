from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from Blog.api.serializers import BlogPostSerializer
from Blog.models import BlogPost


@csrf_exempt
@api_view(['GET', ])
def blogpost_detail_view(request, slug):
    try:
        blog_post = BlogPost.objects.get(slug=slug)
    except BlogPost.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = BlogPostSerializer(blog_post)
        return Response(serializer.data)
        # elif request.method == 'POST':
        #     data = JSONParser().parse(request)
        #     serializer = BlogPostSerializer(data=data)
        #     if serializer.is_valid():
        #         serializer.save()
        #         return JsonResponse(serializer.data, status=201)
        #     return JsonResponse(serializer.errors, status=400)


@csrf_exempt
@api_view(['GET', ])
def blogpost_list_view(request):
    """
    List all code BlogPosts, or create a new BlogPost.
    """
    if request.method == 'GET':
        BlogPosts = BlogPost.objects.all()
        serializer = BlogPostSerializer(BlogPosts, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BlogPostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
