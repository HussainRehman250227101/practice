from django.db.models import Q
from .models import Profile,Skill 
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage



def paginate_profile(request,profiles,profiles_per_page):
    page = request.GET.get('page')
    pagination = Paginator(profiles,profiles_per_page)
    
    try:
        profiles = pagination.page(page) 
    except PageNotAnInteger:
        page = 1
        profiles = pagination.page(page) 
    except EmptyPage:
        page = pagination.num_pages
        profiles = pagination.page(page) 

    left_idx = int(page) - 1
    if left_idx<1:
        left_idx=1 
    right_idx = int(page) + 2
    if right_idx > pagination.num_pages:
        right_idx = pagination.num_pages+1
    custom_range = range(left_idx,right_idx)

    return profiles,custom_range

    
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