from django.contrib.auth.models import User, Group
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer, UserSerializer, GroupSerializer


class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tasks to be viewed or edited.
    """
    template_name = 'index.html'
    queryset = Task.objects.all().order_by('priority')
    serializer_class = TaskSerializer
    renderer_classes = (TemplateHTMLRenderer, )

    def get(self, request):
        queryset = Task.objects.all().order_by('priority')
        return Response({'index': queryset})

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

# The ModelViewSet class inherits from GenericAPIView and includes
# implementations for various actions, by mixing in the behavior of
# the various mixin classes.
#
# The actions provided by the ModelViewSet class are .list(), .retrieve(),
# .create(), .update(), and .destroy().

# class StandardViewSet(viewsets.ViewSet):
#     """
#     Example empty viewset demonstrating the standard
#     actions that will be handled by a router class.
#
#     If you're using format suffixes, make sure to also include
#     the `format=None` keyword argument for each action.
#     """
#
#     def list(self, request):
#         pass
#
#     def create(self, request):
#         pass
#
#     def retrieve(self, request, pk=None):
#         pass
#
#     def update(self, request, pk=None):
#         pass
#
#     def partial_update(self, request, pk=None):
#         pass
#
#     def destroy(self, request, pk=None):
#         pass

# from django.contrib.auth.models import User
# from rest_framework import status
# from rest_framework import viewsets
# from rest_framework.decorators import detail_route, list_route
# from rest_framework.response import Response
# from myapp.serializers import UserSerializer, PasswordSerializer
#
# class UserViewSet(viewsets.ModelViewSet):
#     """
#     A viewset that provides the standard actions
#     """
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#     @detail_route(methods=['post'])
#     def set_password(self, request, pk=None):
#         user = self.get_object()
#         serializer = PasswordSerializer(data=request.data)
#         if serializer.is_valid():
#             user.set_password(serializer.data['password'])
#             user.save()
#             return Response({'status': 'password set'})
#         else:
#             return Response(serializer.errors,
#                             status=status.HTTP_400_BAD_REQUEST)
#
#     @list_route()
#     def recent_users(self, request):
#         recent_users = User.objects.all().order('-last_login')
#
#         page = self.paginate_queryset(recent_users)
#         if page is not None:
#             serializer = self.get_serializer(page, many=True)
#             return self.get_paginated_response(serializer.data)
#
#         serializer = self.get_serializer(recent_users, many=True)
#         return Response(serializer.data)
