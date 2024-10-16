from django.urls import path
from . import views

urlpatterns = [
    path("", views.blog_index, name="blog_index"),
    path("post/<int:blog_id>/", views.blog_details, name ="blog_detail"),
    path("category/<category>", views.blog_category, name="blog_category")
]