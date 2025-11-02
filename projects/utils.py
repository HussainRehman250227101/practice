from django.db.models import Q
from .models import Project,Tag 




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