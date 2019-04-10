from django.shortcuts import render
from core.models import Post


# Create your views here.
def blog_index(request):
    context_dict = {}
    limit = 10
    posts = Post.objects.all()

    if not request.user.is_superuser:
        posts = posts.filter(is_published=True)

    context_dict['posts'] = posts[:limit]
    return render(request, template_name='blog.html', context=context_dict)

# def post_view(request):

