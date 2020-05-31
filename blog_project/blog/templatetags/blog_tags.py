from blog.models import Post
from django import template
register=template.Library()

# @register.simple_tag()
# def total_posts():
#     return Post.objects.count()

@register.simple_tag(name='my_tag')
def total_posts():
    return Post.objects.count()

# @register.inclusion_tag('blog/latest_posts123.html')
# def show_latest_posts():
#     letest_posts=Post.objects.order_by('-publish')[:3]
#     return {'letest_posts':letest_posts}

@register.inclusion_tag('blog/latest_posts123.html')
def show_latest_posts(count=3):
    letest_posts=Post.objects.order_by('-publish')[:count]
    return {'letest_posts':letest_posts}

from django.db.models import Count
@register.simple_tag
def get_most_commented_posts(count=5):
    return Post.objects.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]
