from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import permission_required
from diyblog.models import Post, Comment, Category, Tag
from diyblog.forms import CommentForm


# Create your views here.


# blog_index will render all the blogs
def blog_index(request):
    posts = Post.objects.all().order_by("-publish_date")
    context ={
        "posts":posts,
    }

    return render(request, 'blog/index.html', context)

# blog_details will render the full blog post, with related comments, and forms (if-any)

def blog_details(request, blog_id):
    post = Post.objects.get(pk=blog_id)
    form = CommentForm()

    # Handle POST request (only if the user has 'add_comment' permission)
    if request.method == "POST":
        return handle_comment_post(request, post)

    # Handle GET request (show the blog post and comments)
    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": CommentForm(),
    }

    return render(request, "blog/detail.html", context)

# This function handles the comment submission, with permission enforcement
@permission_required('diyblog.add_comment', raise_exception=True)
def handle_comment_post(request, post):
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = Comment(
            author=form.cleaned_data["author"],
            body=form.cleaned_data["body"],
            post=post,
        )
        comment.save()
        return HttpResponseRedirect(request.path_info)

    # If the form is invalid, show the blog post again with the form errors
    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": form,
    }

    return render(request, "blog/detail.html", context)
    
# blog_category() will filter blogs based on a specific category
def blog_category(request, category):
    posts = Post.objects.filter (
        category__category_name = category
    ).order_by("-publish_date")
    context = {
        "category": category,
        "posts": posts
    }
    return render(request,"blog/category.html", context)


