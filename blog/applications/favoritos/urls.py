from django.urls import path
from . import views

app_name='favorito_app'

urlpatterns = [
    path('perfil/', views.UserPageListView.as_view(), name='Perfil'),
    path('add-entrada/<pk>/', views.AddFavoritosView.as_view(), name='Add-entrada'),
    path('delete-entrada/<pk>/', views.FavoritesDeleteView.as_view(), name='Delete-entrada'),
]