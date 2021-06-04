from django.urls import path

from core.views import UserCreateView, hello, UserListView


urlpatterns = [
    path('', UserListView.as_view(), name='users-list'),
    path('add/', UserCreateView.as_view(), name='users-create'),
]
