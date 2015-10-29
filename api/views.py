from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Activity, Stat
from .serializers import UserSerializer, StatSerializer, ActivitySerializer
# from .permissions import IsUserOrReadOnly
from django.contrib.auth.models import User
# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class ActivityViewSet(viewsets.ModelViewSet):
    """API endpoint for activity view"""
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,
    #                       IsUserOrReadOnly)

    def get_serializer_class(self):
        if self.action == 'list':
            return ActivitySerializer
        else:
            return ActivitySerializer


class StatViewSet(viewsets.ModelViewSet):
    queryset = Stat.objects.all()
    serializer_class = StatSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        activity_pk = self.kwargs['activity_pk']
        return self.queryset.filter(activity_id=activity_pk)
