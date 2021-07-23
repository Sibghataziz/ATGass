from django.shortcuts import render,redirect
from .form import Add_Post
from django.contrib import messages
from .models import Post
from accounts.models import User,Profile

# Create your views here.
def create_post(request):
    if request.method == 'POST':
        user_name=request.user.username
        robj=User.objects.get(username=user_name)
        pobj=Profile.objects.get(user=robj.id)
        if pobj.typ != "Patient":
            new_post = Add_Post(request.POST,request.FILES)
            if new_post.is_valid():
                post = new_post.save(commit=False)
                post.author = robj
                post.save()
                return redirect("home")
            else:
                return redirect("home")
        else:
            return redirect("home")
    else:
        new_post=Add_Post
        return render(request,'post\Add_post.html',{'form':new_post})

def home_view(request):
    user_name=request.user.username
    robj=User.objects.get(username=user_name)
    pobj=Profile.objects.get(user=robj.id)
    if pobj.typ == "Patient":
        posts=Post.objects.filter(draft=False)
    else:
        posts=Post.objects.filter(author=robj)
    return render(request,'post\home.html',{'posts':posts,"profile":pobj})

def post_detail_view(request, id):
    obj = Post.objects.get(id=id)
    context = {
        "object": obj,
    }
    return render(request, "post/post_detail.html", context)
