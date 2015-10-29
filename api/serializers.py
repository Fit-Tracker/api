from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Activity, Stat


class StatSerializer(serializers.HyperlinkedModelSerializer):
    activity_id = serializers.PrimaryKeyRelatedField(
        many=False, read_only=True, source='activity')
    timestamp = serializers.DateField()

    class Meta:
        model = Stat
        fields = ('pk', 'activity_id', 'stat', 'timestamp')

    def create(self, validated_data):
        validated_data['activity_id'] = self.context['activity_pk']
        answer = Stat.objects.create(**validated_data)
        return answer


class ActivitySerializer(serializers.HyperlinkedModelSerializer):
    title = serializers.CharField(max_length=255)

    class Meta:
        model = Activity
        fields = ('id', 'title', 'user')


class ActivityDetailSerializer(ActivitySerializer):
    stats = StatSerializer(many=True, read_only=True)

    class Meta(ActivitySerializer.Meta):
        fields = tuple(list(ActivitySerializer.Meta.fields) + ['stats'])


class UserSerializer(serializers.HyperlinkedModelSerializer):
    activities = ActivitySerializer(many=True, read_only=True)
    stats = StatSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('pk', 'username', 'password', 'activities', 'stats')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
