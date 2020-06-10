from rest_framework import serializers
from .models import Users, UserAuth, Categories, Subscribers, Topics, SubCategories, Comment, TopicStatistic


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


class TopicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Topics
        fields = ['title', 'content', 'user', 'sub_cat', 'category']


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['topic', 'content', 'user']


class SubscriberSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscribers
        fields = ['user', 'topic', 'is_liked']
