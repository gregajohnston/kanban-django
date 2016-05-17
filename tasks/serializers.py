from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Task
        fields = ('id', 'owner', 'title',
                  'description', 'status', 'priority', )


class UserSerializer(serializers.HyperlinkedModelSerializer):
    tasks = serializers.PrimaryKeyRelatedField(
            many=True, queryset=Task.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'tasks', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
