from django.db.models import Q
from .models import Project,Tag 
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage



def paginate_projects(request,projects,projects_per_page):
    page = request.GET.get('page')
    pagination = Paginator(projects,projects_per_page)
    
    try:
        projects = pagination.page(page) 
    except PageNotAnInteger:
        page = 1
        projects = pagination.page(page) 
    except EmptyPage:
        page = pagination.num_pages
        projects = pagination.page(page) 

    left_idx = int(page) - 1
    if left_idx<1:
        left_idx=1 
    right_idx = int(page) + 2
    if right_idx > pagination.num_pages:
        right_idx = pagination.num_pages+1
    custom_range = range(left_idx,right_idx)

    return projects,custom_range



def search_projects(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
            
    projects = Project.objects.distinct().filter(
        Q(title__icontains=search_query) |
        Q(owner__name__icontains = search_query) |
        Q(tag__name__icontains =search_query)
    )

    return projects, search_query