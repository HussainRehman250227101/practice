from django.shortcuts import render,redirect
from .models import Profile

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