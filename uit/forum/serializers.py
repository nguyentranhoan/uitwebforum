from rest_framework import serializers
from .models import Users, UserAuth, Subscribers, Topics, Comment, TopicStatistic, IsLikedTopic


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topics
        fields = ['point']


class ChoiceSerializer(serializers.ModelSerializer):
    choice_result = ResultSerializer(many=True, read_only=True)

    class Meta:
        model = Topics
        fields = ['id', 'question', 'choice_text', 'votes', 'choice_result']


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True)
    queryset = Topics.objects.all()
    # question_result = ResultSerializer(queryset, many=True, read_only=True)

    class Meta:
        model = Topics
        fields = ['id', 'question_text', 'pub_date', 'choices']


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = ['username', 'email', 'password', 'avatar']


class ListUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = ['id', 'username']


class TopicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Topics
        fields = ['id', 'user', 'content']


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
        fields = ['user', 'topic']


class IsLikedTopicSerializer(serializers.ModelSerializer):

    class Meta:
        model = IsLikedTopic
        fields = ['user', 'topic']


class TopicCommentSerializer(serializers.ModelSerializer):
    topic_comment = ListCommentSerializer(many=True, read_only=True)
    queryset = Topics.objects.all()

    class Meta:
        model = Topics
        fields = ['id', 'content', 'topic_comment']


class UserLikedTopicSerializer(serializers.ModelSerializer):
    user_likes_topic = IsLikedTopicSerializer(many=True, read_only=True)
    user_topic = TopicSerializer(many=True, read_only=True)
    user_comment = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Users
        fields = ['username', 'user_topic', 'user_comment', 'user_likes_topic']
