from django.forms import ModelForm 
from .models import Profile, Skill 

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
