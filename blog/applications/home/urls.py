#
from django.urls import path
from . import views

app_name = "home_app"

urlpatterns = [
    path(
        '', 
        views.HomePageView.as_view(),
        name='Index',
    ),
    path(
        'register-suscription/', 
        views.SuscriberCreateView.as_view(),
        name='Register',
    ), 
    path(
        'contact/', 
        views.ContactCreateView.as_view(),
        name='Contact',
    ), 
]