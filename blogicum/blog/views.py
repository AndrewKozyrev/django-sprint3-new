from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from .models import Category, Post


POSTS_ON_MAIN_PAGE = 5


def get_published_posts(posts):
    return posts.select_related(
        'category',
        'location',
        'author',
    ).filter(
        is_published=True,
        pub_date__lte=timezone.now(),
        category__is_published=True,
    )


def index(request):
    context = {
        'post_list': get_published_posts(
            Post.objects.all()
        )[:POSTS_ON_MAIN_PAGE],
    }
    return render(request, 'blog/index.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(
        get_published_posts(Post.objects.all()),
        pk=post_id,
    )
    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True,
    )
    context = {
        'category': category,
        'post_list': get_published_posts(
            Post.objects.filter(category=category)
        ),
    }
    return render(request, 'blog/category.html', context)
