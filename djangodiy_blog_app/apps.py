from django.apps import AppConfig


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField' 
    name = 'djangodiy_blog_app'
    label = "blog"
