from django.shortcuts import render,redirect
from .models import Profile
from .forms import Profile_Form, Skill_Form

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
            # form.save_m2m()
            return redirect('single_user', pk= profile.id)
    context={'form': form}
    return render(request,'users/add_skill.html',context)