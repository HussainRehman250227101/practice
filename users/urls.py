from django.urls import path 
from . import views
urlpatterns = [
    path('',views.all_users, name='all_users'),
    path('single_user/<str:pk>/',views.single_user, name='single_user'),
    path('add_skill/',views.add_skill, name='add_skill'),
    path('edit_skill/<str:pk>/',views.edit_skill, name='edit_skill'),
    path('delete_skill/<str:pk>/',views.delete_skill, name='delete_skill'),
    path('account/<str:pk>/',views.account, name='account'),
    path('edit_profile/<str:pk>/',views.edit_profile, name='edit_profile'),
    path('delete_profile/<str:pk>/',views.delete_profile, name='delete_profile'),
    path('register/',views.register, name='register'),
    path('login/',views.login_view, name='login'),
    path('logout/',views.logout_view, name='logout'),
    
]
