from django.db import models
import uuid 
from users.models import Profile,Skill

class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default= uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.name)


class Project(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(default='images/default.jpg', upload_to='images/')
    tag = models.ManyToManyField(Tag, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True) 
    vote_total = models.IntegerField(default=0, null=True, blank=True) 
    demo_link = models.CharField(max_length=200)
    source_link = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default= uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.title) 
    
    @property
    def review_count(self):
        review_total = self.review_set.all()
        total_votes = review_total.count()
        up_votes = review_total.filter(value = 'up').count() 
        if total_votes:
            ratio = (up_votes/total_votes)*100 
            self.vote_ratio = ratio 
            self.vote_total = total_votes 
            self.save()

    @property
    def reviewers_ids(self):
        reviewers = self.review_set.all().values_list('owner__id', flat=True)
        return reviewers
class Review(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True )
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True)
    votes = [('up', 'up vote'),('down', 'down vote')]
    value = models.CharField(max_length=200, choices=votes)
    body = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default= uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return f'{self.project} --------- {self.value} ' 
    
    