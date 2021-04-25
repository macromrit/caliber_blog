from django.urls import path, include
from . import views

app_name = 'details'

urlpatterns = [
    path('', views.all_blogs, name="all_blogs"),
    path('<int:blog_id>/', views.specified, name="specified"),
    path('post/', views.postings, name="postings"),
]