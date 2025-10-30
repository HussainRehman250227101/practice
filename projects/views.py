from django.shortcuts import render
from .forms import Project_Form
from .models import Project,Tag,Review

# ALL PROJECTS
def all_projects(request):
    projects = Project.objects.all()
    context = {'projects' : projects}
    return render(request, 'projects/all_projects.html',context) 

