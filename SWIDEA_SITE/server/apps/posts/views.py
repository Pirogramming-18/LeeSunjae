from django.shortcuts import render, redirect

from server.apps.posts.models import Post

# Create your views here.


def posts_list(request, *args, **kwargs):
    posts = Post.objects.all()
    return render(request, "posts/posts_list.html", {"postdatas": posts})

def posts_retrieve(request,pk,*args ,**kwargs):
    post = Post.objects.all().get(id=pk)
    return render(request, "posts/posts_retrieve.html", {"postdatas": post})

def posts_create(request,*args, **kwargs):
    if request.method == "POST":
        Post.objects.create(
            title=request.POST["title"],
            # user=request.POST["user"],
            interest=request.POST["interest"],
            price=request.POST["price"],
            content=request.POST["content"],
            image=request.FILES.get("image"),
            
        )
        # go to mainpage
        new = Post.objects.last()
        return redirect(f"/posts/{new.id}")
    return render(request, "posts/posts_create.html")

def posts_delete(request, pk, *args, **kwargs):
    if request.method == "POST":
        post = Post.objects.get(id=pk)
        post.delete()
    return redirect("/")

def posts_update(request, pk, *args, **kwargs):
    post = Post.objects.get(id=pk)
    
    if request.method == "POST":
        post.title = request.POST["title"]
        # post.user = request.POST['user']
        post.interest = request.POST['interest']
        post.price = request.POST['price']
        post.content = request.POST['content']
        post.image = request.FILES.get("image")
        post.save()
        return redirect(f"/posts/{post.id}")
    
    return render(request, "posts/posts_update.html", {"post":post})