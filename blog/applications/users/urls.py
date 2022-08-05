#
from django.urls import path

from . import views

app_name = "users_app"

urlpatterns = [
    path(
        'register/', 
        views.UserRegisterView.as_view(),
        name='Register',
    ),
    path(
        'login/', 
        views.LoginUser.as_view(),
        name='Login',
    ),
    path(
        'logout/', 
        views.LogoutView.as_view(),
        name='Logout',
    ),
    # path(
    #     'update/', 
    #     views.UpdatePasswordView.as_view(),
    #     name='Update',
    # ),
]