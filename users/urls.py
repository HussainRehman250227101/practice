from django.urls import path 
from . import views
urlpatterns = [
    path('',views.all_users, name='all_users'),
    path('single_user/<str:pk>/',views.single_user, name='single_user'),
]
