from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.blog_post_details_page, name='blog_post_details'),
]
