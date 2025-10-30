from django.shortcuts import render,redirect
from .forms import Project_Form,Review_Form
from .models import Project,Tag,Review

# ALL PROJECTS
def all_projects(request):
    projects = Project.objects.all()
    context = {'projects' : projects}
    return render(request, 'projects/all_projects.html',context) 

def single_project(request,pk):
    project = Project.objects.get(id=pk)
    form = Review_Form
    if request.method == 'POST':
        form = Review_Form(request.POST)
        review = form.save(commit=False)
        review.project = project
        review.save()
        return redirect('single_project', pk= project.id)
    context = {'project': project,'form':form}
    return render(request, 'projects/single_project.html', context)