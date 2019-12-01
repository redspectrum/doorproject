from django.shortcuts import render
from django.views.decorators.http import require_POST, require_GET, require_safe, require_http_methods

from .models import Post, Author, Book
from django.db.models import Q
# Create your views here.

def index(request):
    search_query = request.GET.get('search', '')

    if search_query:
        posts = Post.objects.filter(Q(title__icontains=search_query) | Q(body__icontains=search_query))
    else:
        posts = Post.objects.all()

    context = {'name': 'Meat',
               'posts': posts}

    # if request.method == 'POST':
    #
    # else:
    #     form = NameForm()
    return render(request, template_name='blog/index.html', context=context)

@require_POST
def welcome_db(request):
    context = {'name': 'Meat'}
    return render(request, template_name='blog/index.html', context=context)