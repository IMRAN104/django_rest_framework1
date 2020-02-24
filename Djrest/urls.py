from django.contrib import admin
from django.urls import include, path
from Blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Updates.urls')),
    path('blog/', include('Blog.urls')),
    path('blog-create/', views.blog_post_create_view, name='blog_post_create'),
    path('contact/', views.contact, name='contact'),

]
