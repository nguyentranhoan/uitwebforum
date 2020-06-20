from rest_framework import serializers

from .models import Users, Subscribers, Topics, Comment, IsLikedTopic, Categories


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = ['id', 'username', 'email', 'password', 'avatar']


class ListUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = ['id', 'username', 'email', 'avatar']

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Categories
        fields = ['id', 'name', 'is_active', 'created_at', 'parent']


class TopicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Topics
        fields = ['id', 'user', 'content', 'category', 'title', 'created_at']


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['id', 'user', 'topic', 'content']


class UpdateCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['id', 'content']


class ListCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['user', 'content', 'created_at']
        ordering = ['created_at']


class SubscriberSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscribers
        fields = ['id', 'user', 'topic']


class IsLikedTopicSerializer(serializers.ModelSerializer):

    class Meta:
        model = IsLikedTopic
        fields = ['id', 'user', 'topic']


class TopicCommentSerializer(serializers.ModelSerializer):
    topic_comment = ListCommentSerializer(many=True, read_only=True)
    queryset = Topics.objects.all()

    class Meta:
        model = Topics
        fields = ['id', 'content', 'topic_comment']


class UserTotalInfoSerializer(serializers.ModelSerializer):
    user_likes_topic = IsLikedTopicSerializer(many=True, read_only=True)
    user_topic = TopicSerializer(many=True, read_only=True)
    user_comment = CommentSerializer(many=True, read_only=True)
    user_subscriber = SubscriberSerializer(many=True, read_only=True)

    class Meta:
        model = Users
        fields = ['id', 'username', 'user_topic', 'user_comment', 'user_likes_topic', 'user_subscriber']
