from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Activity, Stat


class StatSerializer(serializers.HyperlinkedModelSerializer):
    activity_id = serializers.PrimaryKeyRelatedField(
        many=False, read_only=True, source='activity')
    timestamp = serializers.DateField()
    # title = serializers.PrimaryKeyRelatedField(
    #     source='activity')

    class Meta:
        model = Stat
        fields = ('pk', 'activity_id', 'stat', 'timestamp')


class ActivitySerializer(serializers.HyperlinkedModelSerializer):
    title = serializers.CharField(max_length=255)

    class Meta:
        model = Activity
        fields = ('pk', 'title', 'user')


class ActivityDetailSerializer(ActivitySerializer):
    pass


class UserSerializer(serializers.HyperlinkedModelSerializer):
    activities = ActivitySerializer(many=True, read_only=True)
    stats = StatSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('pk', 'username', 'password', 'activities', 'stats')
