from django.contrib import admin
from django.db.models import indexes
from django.shortcuts import render
from django.http.response import HttpResponse
from django.urls.base import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView

from core.models import User
from core.forms import MyUserCreationForm

def hello(request):
    admin = User.objects.first()
    return render(request, 'index.html', context={"user": admin})


class UserListView(ListView):
    model = User
    # queryset = User.objects.all()
    template_name = 'index.html'


class UserCreateView(CreateView):
    model = User
    form_class = MyUserCreationForm

    success_url = reverse_lazy('users-list')
