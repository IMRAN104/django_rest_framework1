from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.blog_post_list_view, name='blog_post_list'),
    path('<str:slug>/', views.blog_post_details_view, name='blog_post_details'),
    path('<str:slug>/', views.blog_post_update_view, name='blog_post_update'),
    path('<str:slug>/', views.blog_post_delete_view, name='blog_post_delete'),
]
