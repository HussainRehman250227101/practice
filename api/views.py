from rest_framework.decorators import api_view
from rest_framework.response import Response 
from .serializers import project_serializer
from projects.models import Project

@api_view(['GET'])
def get_routes(request):
    routes = [
        {'GET':'api/projects'},
        {'GET':'api/projects/id'},
        {'POST':'api/projects/id/vote'},

        # DEFAULT ROUTES
        {'POST':'api/users/token'},
        {'POST':'api/users/token/refresh'},
       
    ]
    return Response(routes)

@api_view(['GET'])
def get_projects(request):
    projects = Project.objects.all()
    serializer = project_serializer(projects, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def get_project(request,pk):
    projects = Project.objects.get(id=pk)
    serializer = project_serializer(projects, many=False)
    return Response(serializer.data)