from rest_framework import serializers
from . import models

class ImageSerializer(serializers.Serializer):

    class Meta:
        model = models.Image
        field = '__all__'

class CommentSerializer(serializers.Serializer):

    class Meta:
        model = models.Comment
        field = '__all__'

class LikeSerializer(serializers.Serializer):

    class Meta:
        model = models.Like
        field = '__all__'