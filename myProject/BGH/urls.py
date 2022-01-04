from django.urls import path
from . import views


urlpatterns = [
    path('', views.bgh, name='bgh'),
    path('bgh_result/', views.bgh_result, name='bgh_result'),
]