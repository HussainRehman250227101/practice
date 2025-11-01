from django.db.models.signals import post_save,post_delete,pre_delete
from django.contrib.auth.models import User 
from django.conf import settings
from django.core.mail import send_mail
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
        subject = f'Welcome to devsearch {profile.name}!'
        body = f'Welcome at DevSearch developer community, we are glad to have "{profile.name}" with us, feel free to explore and connect with fellow developers, Cheers!'
        send_mail(
            subject,
            body,
            settings.EMAIL_HOST_USER,
            [profile.email],
            fail_silently=False,
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
