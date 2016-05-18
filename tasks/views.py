from django.contrib.auth.models import User, Group
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer, UserSerializer, GroupSerializer


class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tasks to be viewed or edited.
    """
    # view_name = 'api:task-list'
    # if view_name == 'api:task-list':
    #     template_name = 'tasks.html'
    #     renderer_classes = (TemplateHTMLRenderer, )

    queryset = Task.objects.all().order_by('priority')
    serializer_class = TaskSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

    def get(self, request):
        queryset = User.objects.all()
        return Response({'users': queryset})


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


def index(request):
    if request.user.is_admin():
        tasks = Task.objects.all()
    else:
        tasks = Task.objects.filter(user=request.user)

    context = {'tasks': tasks}
    return render(request, 'rest_framework/tasks.html', context)
