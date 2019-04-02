from django.shortcuts import render
from core.models import Post


# Create your views here.
def blog_index(request):
    context_dict = {}

    if request.user.is_superuser:
        context_dict['posts'] = Post.objects.all()
    else:
        context_dict['posts'] = Post.objects.filter(is_published=True)

    return render(request, template_name='index.html', context=context_dict)
