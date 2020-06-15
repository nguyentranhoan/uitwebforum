from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets

from .models import Users, Topics, Comment, Subscribers, IsLikedTopic, TopicStatistic
from .serializers import QuestionSerializer, UserSerializer, TopicSerializer, CommentSerializer, SubscriberSerializer, \
    IsLikedTopicSerializer, TopicCommentSerializer, UserLikedTopicSerializer, ListUserSerializer, \
    UpdateCommentSerializer
from rest_framework import status
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token


# from django.contrib.auth.models import User
@api_view(['GET'])
def home(request):
    return Response({"message": "Welcome home"},
                    status=status.HTTP_200_OK)


@csrf_exempt
@api_view(['POST'])
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    # print(username, "\n", password)
    info = Users.objects.filter(username=username, password=password).first()
    if info is None:
        return Response({"message": "user does not exist!"})
    else:
        return Response(info.id)


@api_view(['POST'])
def register(request):
    username = request.data.get("username")
    password = request.data.get("password")
    email = request.data.get("email")
    # print(username, "\n", password)
    info = Users.objects.create(username=username, password=password, email=email)
    if info is None:
        return Response({"message": "user does not exist!"})
    else:
        return Response(info.id)


@api_view(['POST'])
def forgot_password(request):
    email = request.data.get("email")
    password = request.data.get("password")
    # print(username, "\n", password)
    info = Users.objects.filter(email=email).first()
    if info is None:
        return Response({"message": "user does not exist!"})
    else:
        data = Users.objects.filter(email=email).update(password=password)
        return Response(info.username )


class UserInfo(generics.RetrieveUpdateAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer


class ListTopic(generics.ListCreateAPIView):
    queryset = Topics .objects.all()
    serializer_class = TopicSerializer


def createTopicStatistic(topic_id):
    statistic = TopicStatistic.objects.filter(topic__id=topic_id).first()
    topic_object = Topics.objects.get(pk=topic_id)
    if statistic is None:
        topic_statistic = TopicStatistic.objects.create(topic=topic_object)
        return Response(topic_statistic.views)
    else:
        return Response("Topic statistic exists!!!")


# class TopicCreation(generics.CreateAPIView):
#     queryset = Topics .objects.all()
#     serializer_class = TopicSerializer
@api_view(['POST'])
def createTopic(request):
    user_id = request.data.get("user_id")
    content = request.data.get("content")
    user = Users.objects.get(pk=user_id)
    if user is None:
        return Response("user does not exist!")
    else:
        topic = Topics.objects.create(user=user, content=content)
        createTopicStatistic(topic.id)
        return Response(topic.id)


class CommentCreation(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentUpdate(generics.UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = UpdateCommentSerializer


def createTopicStatistic(topic_id):
    statistic = TopicStatistic.objects.filter(topic__id=topic_id).first()
    topic_object = Topics.objects.get(pk=topic_id)
    if statistic is None:
        topic_statistic = TopicStatistic.objects.create(topic=topic_object)
        return Response(topic_statistic.views)
    else:
        return Response("Topic statistic exists!!!")


@api_view(['POST'])
def subsTopic(request):
    user_id = request.data.get("user_id")
    topic_id = request.data.get("topic_id")
    info = Subscribers.objects.filter(user__id=user_id, topic__id=topic_id).first()
    user = Users.objects.get(pk=user_id)
    topic = Topics.objects.get(pk=topic_id)
    if info is None:
        subscriber = Subscribers.objects.create(user=user,topic=topic)
        return Response(subscriber.id)
    else:
        return Response(f"Topic: '{topic.content}' is already subscribed by user: {user.username}")


@api_view(['POST'])
def LikedTopic(request):
    user_id = request.data.get("user_id")
    topic_id = request.data.get("topic_id")
    user = Users.objects.get(pk=user_id)
    topic = Topics.objects.get(pk=topic_id)
    info = IsLikedTopic.objects.filter(user=user_id, topic=topic_id)[:1].get()
    if info.is_liked:
        print(info.is_liked)
        IsLikedTopic.objects.filter(user=user_id, topic=topic_id).update(is_liked=False)
    else:
        print(info.is_liked)
        IsLikedTopic.objects.filter(user=user_id, topic=topic_id).update(is_liked=True)
    return Response(info.id)


class SubscriberCreate(generics.CreateAPIView):
    queryset = Subscribers.objects.all()
    serializer_class = SubscriberSerializer


class IsLikedTopicCreate(generics.CreateAPIView):
    queryset = IsLikedTopic.objects.all()
    serializer_class = IsLikedTopicSerializer


@api_view(['POST'])
def DislikeTopic(request):
    user_id = request.data.get("user")
    topic_id = request.data.get("topic")
    info = IsLikedTopic.objects.filter(user=user_id, topic=topic_id).first()
    if info is None:
        return Response("User has not liked this topic yet!!!")
    else:
        info.delete()
        return Response(f"User: {user_id} no longer likes this topic: {topic_id}")


class ListUserForSupportListTopicComment(generics.CreateAPIView):
    queryset = Users.objects.all()
    serializer_class = ListUserSerializer


class ListTopicComment(generics.CreateAPIView):
    queryset = Topics.objects.all()
    serializer_class = TopicCommentSerializer


class TestTest(generics.RetrieveAPIView):
    queryset = Users.objects.all()
    serializer_class = UserLikedTopicSerializer
