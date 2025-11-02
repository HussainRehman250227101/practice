from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import Project_Form,Review_Form
from.utils import search_projects
from .models import Project 

# ALL PROJECTS
def all_projects(request):
    projects , search_query = search_projects(request)
    
    context = {'projects' : projects,'search_query':search_query}
    return render(request, 'projects/all_projects.html',context) 


# SINGLE PROJECT
def single_project(request,pk):
    project = Project.objects.get(id=pk) 
    form = Review_Form()
    if request.method == 'POST':
        form = Review_Form(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.project = project 
            review.owner = request.user.profile
            review.save()
            project.review_count
            project.reviewers_ids
            messages.success(request,'Review added successfully')
            return redirect('single_project', pk= project.id)
        else:
            messages.error(request,'An error occured,try again')
    context = {'project': project,'form':form,'all_id':project.reviewers_ids}
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
            messages.success(request,'Project added successfully')
            return redirect('all_projects')
        else:
            messages.error(request,'An error occured,try again')
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
            messages.success(request,'Project updated successfully')
            return redirect('account', pk = profile.id)
        else:
            messages.error(request,'An error occured,try again')
    context={'form':form}
    return render(request,'projects/edit_project.html',context) 

# DELETE PROJECT
def delete_project(request,pk):
    profile = request.user.profile 
    project = profile.project_set.get(id=pk)
    if request.method =='POST':
        project.delete()
        messages.success(request,'Project deleted successfully')
        return redirect('account', pk = profile.id)
    else:
        messages.error(request,'An error occured,try again')
    context = {'object':project}
    return render(request,'delete.html',context)
 
