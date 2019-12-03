from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('send_email/', send_email, name='send_email')
]
