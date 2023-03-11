from django.shortcuts import render, get_object_or_404
from .models import Post, Group


POSTS = 10
def index(request):
    posts = Post.objects.order_by('-pub_date')[:POSTS]
    context = {
        'posts': posts,
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

def group_list(request):
    title = 'Информация о группах проекта Yatube'
    context = {
        'title': title,
    }
    return (request, 'posts/group_list.html', context)