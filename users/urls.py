# ticket/users/urls.py

from django.urls import path
from .views import RoleBasedLoginView
from django.contrib.auth import views as auth_views

app_name = 'users'

urlpatterns = [
    path(
        '',
        RoleBasedLoginView.as_view(),
        name='login'
    ),
    path(
        'logout/',
        auth_views.LogoutView.as_view(next_page='users:login'),
        name='logout'
    ),
]

