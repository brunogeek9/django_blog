from django.shortcuts import render
from blog.models import Post
# Create your views here.


def home(request):
    posts = Post.objects.all()
    # for item in posts:
    #     print(item.content)
    return render(request, 'home.html', {'posts': posts})
