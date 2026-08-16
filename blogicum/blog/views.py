from django.http import Http404
from django.shortcuts import render


def index(request):
    template = 'blog/index.html'
    context = {'posts': posts[::-1]}
    return render(request, template, context)


def post_detail(request, id):
    template = 'blog/detail.html'
    for post in posts:
        if post['id'] == id:
            break
    else:
        raise Http404(f'Публикация с id {id} не найдена')
    context = {'post': post}
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    context = {'category_slug': category_slug}
    return render(request, template, context)
