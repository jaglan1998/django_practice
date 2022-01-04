from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('SignBoard/', include('SignBoard.urls')),
    path('BGH/', include('BGH.urls')),
]