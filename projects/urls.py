from django.urls import path
from . import views
urlpatterns = [
    path('',views.all_projects, name='all_projects'),
    path('single_project/<str:pk>/',views.single_project,name='single_project'),
    path('add_project/',views.add_project,name='add_project'),
    path('edit_project/<str:pk>/',views.edit_project,name='edit_project'),
    path('delete_project/<str:pk>/',views.delete_project,name='delete_project'),

]