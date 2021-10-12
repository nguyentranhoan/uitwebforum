from rest_framework import serializers

from .models import Users, Subscribers, Topics, Comment, IsLikedTopic, IsLikedComment, Categories


class UpdateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = ['username', 'email', 'password', 'avatar']


class ListCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Categories
        fields = ['id', 'name', 'parent']


class ListUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = ['id', 'username', 'email', 'avatar']


class TopicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Topics
        fields = ['id', 'user', 'category', 'title', 'content']


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


class IsLikedCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = IsLikedComment
        fields = ['id', 'user', 'topic', 'comment']


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
        fields = ['id', 'username', "email", 'user_topic', 'user_comment', 'user_likes_topic', 'user_subscriber']
