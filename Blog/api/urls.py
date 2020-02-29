from django.urls import include, path

from . import views

app_name = 'Blog'

urlpatterns = [
    path('', views.blogpost_list_view, name='api_blogpost_list'),
    path('<str:slug>/', views.blogpost_detail_view, name='api_blogpost_details'),
]
