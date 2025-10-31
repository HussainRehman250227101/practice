from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile
from .forms import Profile_Form, Skill_Form,customuserform

# ALL USERS
def all_users(request):
    profiles = Profile.objects.all()
    context ={'profiles':profiles}
    return render(request,'users/all_users.html',context)


# SINGLE USER
def single_user(request,pk):
    profile = Profile.objects.get(id=pk)
    core_skill = profile.skill_set.exclude(description='' )
    other_skill = profile.skill_set.filter(description='' )
    context={'profile':profile,'core_skills':core_skill, 'other_skills':other_skill}
    return render(request,'users/single_user.html',context)

# ADD SKILL
def add_skill(request):
    profile = request.user.profile 
    form = Skill_Form() 
    if request.method =='POST':
        form = Skill_Form(request.POST,request.FILES)
        if form.is_valid():
            form_save = form.save(commit=False)
            form_save.owner = profile 
            form_save.save()
            form.save_m2m()
            messages.success(request,'skill added successfully')
            return redirect('single_user', pk= profile.id)
    context={'form': form}
    return render(request,'users/add_skill.html',context) 

# EDIT SKILL
def edit_skill(request,pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)
    form = Skill_Form(instance=skill)
    if request.method=='POST':
        form = Skill_Form(request.POST,instance=skill)
        if form.is_valid():
            form.save()
            messages.success(request,'skill updated successfully')
            return redirect('account',pk=profile.id)
    context={'form':form}
    return render(request, 'users/add_skill.html', context)


# DELETE SKILL 
def delete_skill(request,pk):
    profile = request.user.profile 
    skill = profile.skill_set.get(id=pk)
    if request.method=='POST':
        skill.delete()
        messages.success(request,'skill deleted successfully')
        return redirect('account',pk=profile.id)
    context = {'object':skill}
    return render(request,'delete.html',context)

# ACCOUNT
def account(request,pk):
    profile = request.user.profile 
    projects = profile.project_set.all()
    core_skills = profile.skill_set.exclude(description='')
    other_skills = profile.skill_set.filter(description='')
    context = {'profile':profile,'core_skills':core_skills,'other_skills':other_skills,'projects':projects}
    return render(request, 'users/account.html',context)

# EDIT PROFILE
def edit_profile(request,pk):
    profile = request.user.profile 
    form = Profile_Form(instance=profile)
    if request.method == 'POST':
        form = Profile_Form(request.POST,request.FILES,instance=profile)
        if form.is_valid():
            form_save = form.save(commit=False)
            form_save.user = request.user 
            form_save.save()
            messages.success(request,'Profile updated successfully')
            return redirect('account', pk=profile.id)


    context= {'form':form,'profile':profile}
    return render(request,'users/edit_profile.html',context) 

# DELETE PROFILE 
def delete_profile(request,pk):
    profile = request.user.profile
    if request.method=='POST':
        profile.delete()
        profile.user.delete()
        messages.success(request,'Profile deleted successfully')
        return redirect('all_projects')
    context = {'object':profile}
    return render(request,'delete.html',context) 

# REGISTER
def register(request):
    page = 'register'
    form = customuserform()
    if request.method =='POST':
        form = customuserform(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request,user)
            messages.success(request,'Profile created successfully')
            return redirect('edit_profile',pk = user.profile.id)
    else:
        print("an error occured")
    context = {'form':form,'page':page}
    return render (request,'users/login_signup.html',context) 

# LOGIN
def login_view(request):
    page = 'login'
    context={'page':page}

    if request.user.is_authenticated:
        return redirect('account',pk=request.user.profile.id)
    
    if request.method =='POST':
        username = request.POST['username'].lower()
        password = request.POST['password']
        try:
            user = User.objects.get(username = username)
        except:
            messages.error(request,"user doesn't exist")
        user = authenticate(request,username=username,password= password)
        if user is not None:
            login(request,user)
            messages.success(request,'logged in successfully')
            return redirect('all_projects')
        else:
            messages.error(request,"username or password is wrong")
    return render(request,'users/login_signup.html',context) 

def logout_view(request):
    logout(request)
    messages.success(request,'logged out')
    return redirect('login')
