from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('sign_board/', views.sign_board, name='sign_board')
]