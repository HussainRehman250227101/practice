from django.db.models.signals import post_save,post_delete,pre_delete
from django.contrib.auth.models import User 
from .models import Profile 

def createprofile(sender,instance,created,**kwargs):
    user = instance
    if created:
        profile = Profile.objects.create(
            user = user,
            name = user.first_name,
            username = user.username,
            email = user.email 
        )

def updateuser(sender,instance,created,**kwargs):
    profile = instance 
    user = profile.user
    if created==False:
        user.username = profile.username
        user.first_name = profile.name 
        user.email = profile.email 
        user.save()
        

     


post_save.connect(createprofile, sender=User)
post_save.connect(updateuser, sender=Profile) 
