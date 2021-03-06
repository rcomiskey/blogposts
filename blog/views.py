from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm
from django.utils import timezone


# Create your views here.
def getposts(request):
   post = Post.objects.all()
   return render(request, "blogposts.html", {'posts': post})
   
def add_post(request):
  if request.method == "POST":
      form = PostForm(request.POST)
      if form.is_valid():
          post = form.save(commit=False)
          post.author = request.user
          post.created_date = timezone.now()
          post.save()
          return redirect(viewpost, post.pk)
  else:
      # GET Request so just give them a blank form
      form = PostForm()    
   
  return render(request, "postform.html", { 'form': form })
  
def viewpost(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request, "viewpost.html", {'post': post})


def editpost(request, id):
    post = get_object_or_404(Post, pk=id)
    
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect(getposts)
        
    else:
        form = PostForm(instance=post)
    
    form = PostForm(instance = post)
    return render(request, "postform.html", { 'form': form})
    
