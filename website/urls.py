from django.urls import path
from . import views


urlpatterns = [
    #path('address bar reference', request-return function name in views.py, html reference name),
    path('', views.home, name='home'), #defining the 'home' route and the view to be called
    path('client/<int:pk>', views.client_record, name='client'),
    path('delete_client/<int:pk>', views.delete_client, name='delete_client'),
    path('add_client/',views.add_client, name='add_client'),
    path('update_client/<int:pk>', views.update_client, name='update_client'),
    path('logout/', views.logout_user, name='logout'),
    path('search_client/', views.search_client, name='search_client'),
    
]