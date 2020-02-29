from django.contrib import admin
from django.urls import include, path

from Blog import views as BlogViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Updates.urls')),
    path('blog/', include('Blog.urls')),
    path('blog-create/', BlogViews.blog_post_create_view, name='blog_post_create'),
    path('contact/', BlogViews.contact, name='contact'),
    path('api/blog/', include('Blog.api.urls', 'blog_api')),
]
