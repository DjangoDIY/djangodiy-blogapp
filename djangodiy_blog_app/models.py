from django.db import models

# Create your models here.


# category model - this will allow admin or traffic to filter blogs based on categories
class Category(models.Model):
    category_name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.category_name
    

# Tag model - this will give tags to blog, traffic can filter blogs based on this
class Tag(models.Model):
    tag_name = models.CharField(max_length=30, unique= True)

    class Meta:
        verbose_name_plural = "Tags"

    def __str__(self):
        return self.tag_name

# Post model - this will contain information about the blog and its contents

class Post(models.Model):
    title = models.CharField(max_length= 255, unique= True)
    subtitle = models.CharField(max_length= 255, blank= True)
    slug = models.CharField(max_length=30, unique= True)
    body = models.TextField()
    meta_description = models.CharField(max_length=150, blank= True)
    date_created = models.DateTimeField(auto_now_add= True)
    date_modified = models.DateTimeField(auto_now= True)
    publish_date = models.DateTimeField(blank= True, null= True)
    published = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, blank= True)
    category = models.ManyToManyField(Category, blank= True)
    
    class Meta: 
        verbose_name_plural = 'Blogs'
        ordering = ["-publish_date"]

    def __str__(self):
        return self.title
    


# Comment model - this allow traffic to leave comments on the post/blog

class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add= True)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author} on {self.post}"


