from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('send_email/', send_email, name='send_email'),
    path('create_letter/', create_letter, name='create_letter'),
    path('all_letters/', all_letters, name='all_letters'),
    path('create/', PostCreate.as_view(), name='create'),
]
