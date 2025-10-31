from django.forms import ModelForm 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Skill , Message

class Profile_Form(ModelForm):
    class Meta: 
        model = Profile 
        fields = ['name','username','email','location','short_intro','bio','profile_image','social_github',
                  'social_linkedin', 'social_youtube','social_twitter','social_website',
                  ]
        labels = {
            'social_github': 'Github',
            'social_youtube': 'Youtube',
            'social_linkedin': 'Linkedin',
            'social_twitter': 'X',
            'social_website': 'Website',
            'name': 'Name',
            'username': 'Username',
        }
    
    def __init__(self,*args,**kwargs):
        super(Profile_Form,self).__init__(*args,**kwargs)
        for key,value in self.fields.items():
            value.widget.attrs.update({'class':'input input--text'}) 


class Skill_Form(ModelForm):
    class Meta:
        model = Skill 
        fields = ['skill_name','description']
        labels = {
            'skill_name':'Name',
            'description':'Description'
        }

    def __init__(self,*args,**kwargs):
        super(Skill_Form,self).__init__(*args,**kwargs)
        for key,value in self.fields.items():
            value.widget.attrs.update({'class':'input input--text'}) 


class customuserform(UserCreationForm):
    class Meta:
        model = User 
        fields = ['first_name','username','email','password1','password2'] 
        labels = {
            'first_name' : 'Name',
            'password1': 'Password',
            'password2': 'Confirm Password'
        }

    def __init__(self,*args,**kwargs):
        super(customuserform,self).__init__(*args,*kwargs)
        for key,values in self.fields.items():
            values.widget.attrs.update({'class':'input input--text'}) 

class Message_Form(ModelForm):
    class Meta:
        model = Message 
        fields = ['subject','body']
        
    def __init__(self,*args,**kwargs):
        super(Message_Form,self).__init__(*args,*kwargs)
        for key,values in self.fields.items():
            values.widget.attrs.update({'class':'input input--text'}) 
