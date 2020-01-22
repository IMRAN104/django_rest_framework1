from django.urls import path
from . import views


urlpatterns = [
    path('', views.json_example_view),
    path('details/', views.details_update_page),
    path('details/<int:integer_field>/', views.details_update_page, name='details-update')
]
