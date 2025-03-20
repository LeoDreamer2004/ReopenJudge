from rest_framework.serializers import ModelSerializer
from .models import *


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"


class ProblemSerializer(ModelSerializer):
    class Meta:
        model = Problem
        fields = "__all__"


class AnnouncementSerializer(ModelSerializer):
    class Meta:
        model = Announcement
        fields = "__all__"
