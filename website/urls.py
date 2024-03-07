from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'), #defining the 'home' route and the view to be called
]