from django.forms import ModelForm 
from django import forms
from .models import Project, Tag, Review 

class Project_Form(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description','image','tag','demo_link','source_link']
        widgets = {
            'tags': forms.CheckboxSelectMultiple()
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
        super(self).__init__(*args,**kwargs)
        for value in self.fields.values():
            value.widget.attrs.update({'class':'input input--text'})
