from django.shortcuts import render
from core.models import Post, Category
from django.http import HttpResponse
import datetime


# Create your views here.
def blog_index(request):
    context_dict = {}
    limit = 10
    posts = Post.objects.all()
    categories = Category.objects.all()

    if not request.user.is_superuser:
        posts = posts.filter(is_published=True)

    context_dict['posts'] = posts[:limit]
    context_dict['categories'] = categories
    return render(request, template_name='blog.html', context=context_dict)


def post_view(request, slug, pk):

    post = Post.objects.get(slug=slug, pk=pk)
    context = {
        "post": post,
    }
    return render(request, "blog_post.html", context)

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)



