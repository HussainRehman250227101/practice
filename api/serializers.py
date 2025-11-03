from rest_framework import serializers
from projects.models import Project,Tag,Review 
from users.models import Profile 

class profile_serializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class tag_serializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class review_serializer(serializers.ModelSerializer):
    class Meta:
        model = Review 
        fields = '__all__'

class project_serializer(serializers.ModelSerializer):
    owner = profile_serializer(many=False)
    tag = tag_serializer(many=True) 
    reviews = serializers.SerializerMethodField() 

    class Meta:
        model = Project 
        fields = '__all__' 

    def get_reviews(self,instance):
        reviews = instance.review_set.all() 
        serializer = review_serializer(reviews,many= True)
        return serializer.data