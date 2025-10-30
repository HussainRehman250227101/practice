from django.shortcuts import render
from .forms import Project_Form
from .models import Project,Tag,Review

# ALL PROJECTS
def all_projects(request):
    projects = Project.objects.all()
    context = {'projects' : projects}
    return render(request, 'projects/all_projects.html',context) 

def single_project(request,pk):
    project = Project.objects.get(id=pk)
    context = {'project': project}
    return render(request, 'projects/single_project.html', context)