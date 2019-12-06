from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST, require_GET, require_safe, require_http_methods
from django.http import HttpResponse

from .models import Post, Author, Book, Task, Letter

from django.db.models import Q
# Create your views here.
from .tasks import send_email_task
from django.core.mail import send_mail
from datetime import datetime
from .forms import LetterForm
from django.views.generic import View


def index(request):
    search_query = request.GET.get('sending_time', '')

    letters = []
    if search_query:
        letters = Letter.objects.filter(Q(title__icontains=search_query) | Q(body__icontains=search_query))
        # posts = Book.objects.select_related('author_book').filter(title__icontains=search_query)

    context = {'name': 'Meat',
               'letters': letters}
    return render(request, template_name='blog/index.html', context=context)


@require_POST
def welcome_db(request):
    context = {'name': 'Meat'}
    return render(request, template_name='blog/index.html', context=context)


def send_email(request):
    time_now = datetime.now()
    letters = Letter.objects.filter(sending_time__lt=time_now).order_by('-sending_time')
    for letter in letters:
        send_email_task(email=letter.email_destination,
                              title=letter.title,
                              body=letter.body
                              )
        letter.delete()
    return redirect(all_letters)


def create_letter(request):
    form = LetterForm()
    return HttpResponse('CREATED!')


def all_letters(request):
    time_now = datetime.now()
    letters = Letter.objects.filter(sending_time__lt=time_now).order_by('-sending_time')

    context = {
        'letters': letters,
        'time_now': time_now.strftime('%d/%m/%Y %H:%M')
    }
    return render(request, template_name='blog/all_letters.html', context=context)


class ObjectCreateMixin:
    model_form = None
    template = None

    def get(self, request):
        form = self.model_form()
        return render(request, self.template, context={'form': form})

    def post(self, request):
        bound_form = self.model_form(request.POST)

        if bound_form.is_valid():
            bound_form.save()
            return redirect(all_letters)
        return render(request, self.template, context={'form': bound_form})


class PostCreate(ObjectCreateMixin, View):
    model_form = LetterForm
    template = 'blog/create_letter.html'
    raise_exception = True
