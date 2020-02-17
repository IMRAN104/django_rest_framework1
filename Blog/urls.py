from django.urls import include, path

from . import views

urlpatterns = [
    path('<str:slug>/', views.blog_post_details_page, name='blog_post_details'),
]
