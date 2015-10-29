
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Activity, Stat
from .serializers import UserSerializer, StatSerializer, ActivitySerializer
from .permissions import IsAskerOrReadOnly
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

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsAskerOrReadOnly)

    # def get_serializer_class(self):
    #     if self.action == 'list':
    #         return ActivitySerializer
    #     else:
    #         return ActivityDetailSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class StatViewSet(viewsets.ModelViewSet):
    queryset = Stat.objects.all()
    serializer_class = StatSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        activity_pk = self.kwargs['activity_pk']
        return self.queryset.filter(activity_id=activity_pk)


@api_view(['GET'])
def whoami(request):
    user = request.user
    if user.is_authenticated():
        serializer = UserSerializer(user)
        return Response(serializer.data)
    else:
        return Response('', status=status.HTTP_404_NOT_FOUND)
