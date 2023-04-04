from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm



# Create your views here.
def index(request):
    #If the method is POST
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        #If the form is valid
        if form.is_valid():
            # Yes, Save
            form.save()
            # Redirect to home
            return HttpResponseRedirect('/')
        else:
             # No, Show Error
            return HttpResponseRedirect(form.errors.as_json())
    # Get all posts, limit = 20
    posts = Post.objects.all().order_by('-created_at')[:20]
    # show 
    return render(request,'post.html',
                  {'posts': posts})

def delete(request, post_id):
    post=Post.objects.get(id=post_id)
    post.delete()
    # output = 'POST ID is' + str(post_id)
    return HttpResponseRedirect("/")


def edit(request, post_id):
    #If the method is POST
    post = Post.objects.get(id = post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        #If the form is valid
        if form.is_valid():
            # Yes, Save
            form.save()
            # Redirect to home
            return HttpResponseRedirect('/')
        else:
             # No, Show Error
            return HttpResponseRedirect(form.errors.as_json())
    # Get all posts, limit = 20

    # show 
    return render(request,'edit.html',
                  {'post': post})


def likes(request, post_id):
    post = Post.objects.get(id = post_id)
    post.like += 1
    post.save()
    return HttpResponseRedirect('/')