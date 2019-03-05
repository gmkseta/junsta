from rest_framework import serializers
from . import models


class ExploreUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = (
            'profile_image',
            'username',
            'name',
            'id'
        )

class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model =models.User
        fields = (
            'username',
            'name',
            'bio',
            'website',
            'post_count',
            'followers_count',
            'following_count'
        )