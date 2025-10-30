from django.shortcuts import render,redirect
from .forms import Project_Form,Review_Form
from .models import Project,Tag,Review

# ALL PROJECTS
def all_projects(request):
    projects = Project.objects.all()
    context = {'projects' : projects}
    return render(request, 'projects/all_projects.html',context) 


# SINGLE PROJECT
def single_project(request,pk):
    project = Project.objects.get(id=pk)
    form = Review_Form()
    if request.method == 'POST':
        form = Review_Form(request.POST)
        review = form.save(commit=False)
        review.project = project
        review.save()
        return redirect('single_project', pk= project.id)
    context = {'project': project,'form':form}
    return render(request, 'projects/single_project.html', context)


# ADD PROJECT
def add_project(request):
    profile = request.user.profile
    form = Project_Form()
    if request.method =='POST':
        form = Project_Form(request.POST,request.FILES)
        if form.is_valid():
            form_save = form.save(commit=False)
            form_save.owner = profile 
            form_save.save()
            form.save_m2m()
            return redirect('all_projects')
    context = {'form':form}
    return render(request, 'projects/add_project.html',context)


# EDIT PROJECT
def edit_project(request,pk):
    profile = request.user.profile
    project = Project.objects.get(id=pk)
    form = Project_Form(instance=project)
    if request.method =='POST':
        form = Project_Form(request.POST,request.FILES,instance=project)
        if form.is_valid():
            form_save = form.save(commit=False)
            form_save.owner = profile 
            form_save.save()
            form.save_m2m()
            return redirect('single_project',pk=project.id )
    context={'form':form}
    return render(request,'projects/edit_project.html',context)