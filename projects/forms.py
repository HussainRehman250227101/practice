from django.forms import ModelForm 
from django import forms
from .models import Project, Tag, Review 

class Project_Form(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description','image','tag','demo_link','source_link']
        widgets = {
            'tag': forms.CheckboxSelectMultiple()
        }
        labels = {
            'title': 'Title',
            'description': 'Description',
            'image': 'Project Image',
            'tag': 'Select Tags',
            'demo_link': 'Demo link',
            'source_link': 'Source link'
        } 
    def __init__(self,*args,**kwargs):
        super(Project_Form,self).__init__(*args,**kwargs)
        for value in self.fields.values():
            value.widget.attrs.update({'class':'input input--text'})

class Review_Form(ModelForm):
    class Meta:
        model = Review
        fields = ['value','body']
        labels = {
            'value': 'Place your vote',
            'body': 'Post a review'
        }
    def __init__(self,*args,**kwargs):
        super(Review_Form,self).__init__(*args,**kwargs)
        for value in self.fields.values():
            value.widget.attrs.update({'class':'input input--text','style':'margin-top:10px;margin-bottom:10px;'})
