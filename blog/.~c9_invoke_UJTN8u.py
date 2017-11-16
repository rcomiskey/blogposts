from django.shortcuts import render, redirect, get_object_or_404
from .models import Post


# Create your views here.
def get_post(request):
   post = Post.objects.all()
   return render(request, "blogposts.html", {'posts': post})
   
# def add_post(request):
#   if request.method == "POST":
#       # Get the details from the request
#       form = TodoItemForm(request.POST)
#       # Handle Saving to DB
#       if form.is_valid():
#           form.save()
#           return redirect(get_index)
#   else:
#       # GET Request so just give them a blank form
#       form = TodoItemForm()    
   
#   return render(request, "item_form.html", { 'form': form })
