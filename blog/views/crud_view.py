from django.shortcuts import render,redirect,get_object_or_404
from ..models import Blogs
from django.contrib.auth.decorators import login_required

@login_required
def create(request):
    if request.method=="POST":
        title=request.POST.get("title")
        subtitle=request.POST.get("subtitle")
        image=request.FILES.get("image")
        description=request.POST.get("description")
        blog=Blogs(title=title,subtitle=subtitle,image=image,description=description,author=request.user)
        blog.save()
        return redirect('home')
    return render(request,'main/create_blog.html')

def edit(request):
    return render(request,'main/edit_blog.html')

def home(request):
    blogs=Blogs.objects.all()
    return render(request,'main/home_page.html',{'blogs': blogs})

def single(request,blog_id):
    blog=get_object_or_404(Blogs,pk=blog_id)
    return render(request,'main/single_blog.html',{'blog':blog})

def delete(request,blog_id):
    blog=get_object_or_404(Blogs,pk=blog_id)
    if blog.author==request.user:
        blog.delete()
    else:
        return redirect('single',blog_id=blog.id)
    #blog.delete()
    return redirect('home')