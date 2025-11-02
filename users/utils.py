from django.db.models import Q
from .models import Profile,Skill 




def search_profiles(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
            
    profiles = Profile.objects.distinct().filter(
        Q(name__icontains=search_query) |
        Q(short_intro__icontains = search_query) |
        Q(skill__skill_name__icontains =search_query)
    )

    return profiles, search_query