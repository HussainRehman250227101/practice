from django.urls import path
from . import views
urlpatterns = [
    path('',views.all_projects, name='all_projects'),
    path('single_project/<str:pk>/',views.single_project,name='single_project')

]