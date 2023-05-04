from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Post, Group, User


POSTS = 10


def index(request):
    post_list = Post.objects.all().order_by('-pub_date')
    paginator = Paginator(post_list, 10) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'posts/index.html', context) 


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    title = 'Записи сообщества'
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:POSTS]
    context = {
        'group': group,
        'title': title,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)


def profile(request, username):
    user_obj = get_object_or_404 (User, username=username)
    posts = user_obj.posts.all()
    ammount_of_posts = posts.count()
    paginator = Paginator (posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page (page_number)
    title = user_obj.get_full_name()
    context = {
        'user_obj' : user_obj,
        'posts' : posts,
        'title' : title,
        'ammount' : ammount_of_posts,
        'page_obj' : page_obj,
    }
    return render(request, 'posts/profile.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {
        'post' : post,
    }
    return render(request, 'posts/post_detail.html', context) 
