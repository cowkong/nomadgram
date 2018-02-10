from rest_framework import serializers
from . import models
from nomadgram.users import models as user_models


class FeedUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = user_models.User
        fields = (
            'username',
            'profile_image'
        )


class CommentSerializer(serializers.ModelSerializer):

    creator = FeedUserSerializer()

    class Meta:
        model = models.Comment
        #fields = '__all__' # all은 사실 전부가 아니다.
        fields = (
            'id',
            'message',
            'creator'
        )


class LikeSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = models.Like
        fields = '__all__'



class ImageSerializer(serializers.ModelSerializer):
    
    comments = CommentSerializer(many =True)
    creator = FeedUserSerializer()

    class Meta:
        model = models.Image
        fields =(
            'id',
            'file',
            'location',
            'creator',
            'caption',
            'comments', # comment모델에서 해당 image의foreign key를 가지고 있는 pk값
            'like_count'
        )

