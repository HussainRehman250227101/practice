from django.db import models
import uuid 

class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default= uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.name)


class Project(models.Model):
    # owner
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(default='images/default.jpg')
    tag = models.ManyToManyField(Tag, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True) 
    vote_total = models.IntegerField(default=0, null=True, blank=True) 
    demo_link = models.CharField(max_length=200)
    source_link = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default= uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.title) 
    

class Review(models.Model):
    # owner
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True)
    votes = [('up', 'up vote'),('down', 'down vote')]
    value = models.CharField(max_length=200, choices=votes)
    body = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default= uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return f'{self.project} --------- {self.value} ' 
    
    