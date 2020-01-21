from django.urls import path
from . import views


urlpatterns = [
    path('', views.json_example_view),

]
