from django.shortcuts import render, HttpResponseRedirect
from blog.models import Post, Comment
from blog.forms import CommentForm


# Create your views here.


# blog_index will render all the blogs
def blog_index(request):
    posts = Post.objects.all().order_by("-publish_date")
    context ={
        "posts":posts,
    }

    return render(request, 'blog/index.html', context)

# blog_details will render the full blog post, with related comments, and forms (if-any)

def blog_details(requst, blog_id):
    post = Post.objects.get(pk = blog_id)
    form = CommentForm()
    if requst.method == "POST":
        form = CommentForm(requst.POST)
        if form.is_valid():
            comment = Comment(
                author = form.cleaned_data("author"),
                body = form.cleaned_data("body"),
                post = post,

            )
            comment.save()
            return HttpResponseRedirect(requst.path_info)
    comments = Comment.objects.filter(post= post)
    context = {
            "post": post,
            "comments": comments,
            "form": CommentForm(),
        }

    return render(requst, "blog/details.html", context)
    
# blog_category() will filter blogs based on a specific category
def blog_category(request, category):
    posts = Post.objects.filter (
        catergory_filter = category
    ).order_by("-publish_date")
    context = {
        "category": category,
        "posts": posts
    }
    return render(request,"blog/category.html", context)


