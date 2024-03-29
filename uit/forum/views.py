from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Users, Topics, Comment, Subscribers, IsLikedTopic, TopicStatistic, IsLikedComment, Categories
from .serializers import TopicSerializer, CommentSerializer, ListUserSerializer, \
    UpdateCommentSerializer, UserTotalInfoSerializer, UpdateUserSerializer, ListCategorySerializer


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
    info = Users.objects.filter(username=username,
                                password=password).first()
    if info is None:
        return Response({"message": "username or password is invalid"})
    else:
        return Response(info.id)


@api_view(['POST'])
def register(request):
    username = request.data.get("username")
    password = request.data.get("password")
    email = request.data.get("email")
    # print(username, "\n", password)
    check_username = Users.objects.filter(username=username).first()
    check_email = Users.objects.filter(email=email).first()
    if check_username is not None:
        return Response({"message": "username already exists,"})
    if check_email is not None:
        return Response({"message": "email already exists,"})

    info = Users.objects.create(username=username,
                                password=password,
                                email=email)
    return Response(info.id)


class UpdateUserInfo(generics.RetrieveUpdateAPIView):
    queryset = Users.objects.all()
    serializer_class = UpdateUserSerializer


@api_view(['POST'])
def forgotPassword(request):
    email = request.data.get("email")
    password = request.data.get("password")
    # print(username, "\n", password)
    info = Users.objects.filter(email=email).first()
    if info is None:
        return Response({"message": "email is not correct."})
    else:
        Users.objects.filter(email=email).update(password=password)
        data = {"id": info.id, "username": info.username}
        return Response(data)


class ListUser(generics.ListAPIView):
    queryset = Users.objects.all()
    serializer_class = ListUserSerializer


@api_view(['GET'])
def listUser(request):
    info = Users.objects.all()
    list_user = []
    for data in info:
        user_info = {"id": data.id,
                     "username": data.username,
                     "email": data.email,
                     "avatar": data.avatar.name}
        list_user.append(user_info)
    return Response(list_user)


class UserTotalInfo(generics.RetrieveAPIView):
    queryset = Users.objects.all()
    serializer_class = UserTotalInfoSerializer


@api_view(['GET'])
def CheckUserLikedTopic(request, user_id, topic_id):
    info = IsLikedTopic.objects.filter(user__id=user_id,
                                       topic__id=topic_id).first()
    if info is None:
        return Response(0)
    else:
        return Response(1)


@api_view(['GET'])
def CheckUserLikedComment(request, user_id, topic_id, comment_id):
    info = IsLikedComment.objects.filter(user__id=user_id,
                                         topic__id=topic_id,
                                         comment__id=comment_id).first()
    if info is None:
        return Response(0)
    else:
        return Response(1)


class ListCategory(generics.ListAPIView):
    queryset = Categories.objects.all()
    serializer_class = ListCategorySerializer


def createTopicStatistic(topic_id):
    statistic = TopicStatistic.objects.filter(topic__id=topic_id).first()
    topic_object = Topics.objects.get(pk=topic_id)
    if statistic is None:
        TopicStatistic.objects.create(topic=topic_object)
    else:
        pass


class CreateTopic(generics.CreateAPIView):
    queryset = Topics.objects.all()
    serializer_class = TopicSerializer


class UpdateTopic(generics.UpdateAPIView):
    queryset = Topics.objects.all()
    serializer_class = TopicSerializer


class ListTopic(generics.ListAPIView):
    queryset = Topics.objects.all()
    serializer_class = TopicSerializer


@api_view(['GET'])
def listTopicComment(request, topic_id):
    topic = Topics.objects.get(pk=topic_id)
    data = {"topic_id": topic.id,
            "content": topic.content}
    comment_list = []
    comment_data = {"comment_data": comment_list}
    list_topic_comment = [data, comment_data]
    if topic is None:
        return Response({"message": "topic is invalid"})
    else:
        comments = Comment.objects.filter(topic__id=topic_id)
        for comment in comments:
            user = Users.objects.get(pk=comment.user_id)
            data = {"user_id": user.id,
                    "user_username": user.username,
                    "content": comment.content,
                    "created_at": comment.created_at}
            comment_list.append(data)
        return Response(list_topic_comment)


@api_view(['POST'])
def createTopic(request):
    user_id = request.data.get("user_id")
    content = request.data.get("content")
    user = Users.objects.get(pk=user_id)
    if user is None:
        return Response({"message": "user is invalid"})
    else:
        topic = Topics.objects.create(user=user,
                                      content=content)
        createTopicStatistic(topic.id)
        return Response(topic.id)


# @api_view(['POST'])
# def LikedTopic(request):
#     user_id = request.data.get("user_id")
#     topic_id = request.data.get("topic_id")
#     info = IsLikedTopic.objects.filter(user=user_id, topic=topic_id)[:1].get()
#     if info.is_liked:
#         print(info.is_liked)
#         IsLikedTopic.objects.filter(user=user_id, topic=topic_id).update(is_liked=False)
#     else:
#         print(info.is_liked)
#         IsLikedTopic.objects.filter(user=user_id, topic=topic_id).update(is_liked=True)
#     return Response(info.id)
#
#
# @api_view(['POST'])
# def DislikeTopic(request):
#     user_id = request.data.get("user")
#     topic_id = request.data.get("topic")
#     info = IsLikedTopic.objects.filter(user=user_id, topic=topic_id).first()
#     if info is None:
#         return Response("User has not liked this topic yet!!!")
#     else:
#         info.delete()
#         return Response(f"User: {user_id} no longer likes this topic: {topic_id}")


@api_view(['GET'])
def countNumberOfLikesComment(request, comment_id):
    info = IsLikedComment.objects.filter(comment__id=comment_id)
    if len(info) == 0:
        return Response({"message": "comment does not exist."})
    number_of_likes = info.count()
    data = {"comment_id": comment_id,
            "number_of_likes": number_of_likes}
    return Response(data)


@api_view(['GET'])
def countNumberOfLikesTopic(request, topic_id):
    info = IsLikedTopic.objects.filter(topic__id=topic_id)
    number_of_likes = info.count()
    data = {"topic_id": topic_id,
            "number_of_likes": number_of_likes}
    return Response(data)


@api_view(['GET'])
def countNumberOfSubscribersTopic(request, topic_id):
    info = Subscribers.objects.filter(topic__id=topic_id)
    number_of_subscribers = info.count()
    data = {"topic_id": topic_id,
            "number_of_subscribers": number_of_subscribers}
    return Response(data)


@api_view(['GET'])
def countNumberOfViews(request, topic_id):
    info = TopicStatistic.objects.filter(topic__id=topic_id)
    number_of_views = info.views
    data = {"topic_id": topic_id,
            "number_of_views": number_of_views}
    return Response(data)


@api_view(['GET'])
def increaseTopicView(request, topic_id):
    topic = Topics.objects.filter(pk=topic_id).first()
    if topic is None:
        return Response({"message": "topic is invalid"})
    else:
        topic_statistic = TopicStatistic.objects.filter(topic__id=topic_id).first()
        if topic_statistic is not None:
            number_of_views = topic_statistic.views
            TopicStatistic.objects.filter(topic__id=topic_id).update(views=number_of_views + 1)
            return Response(number_of_views + 1)
        else:
            createTopicStatistic(topic_id)
            return Response(1)


@api_view(['POST'])
def likeTopic(request):
    user_id = request.data.get("user_id")
    topic_id = request.data.get("topic_id")
    info = IsLikedTopic.objects.filter(user__id=user_id,
                                       topic__id=topic_id).first()
    user = Users.objects.get(pk=user_id)
    topic = Topics.objects.get(pk=topic_id)
    if info is None:
        liker = IsLikedTopic.objects.create(user=user,
                                            topic=topic)
        return Response(liker.id)
    else:
        info.delete()
        return Response(0)


@api_view(['POST'])
def subsTopic(request):
    user_id = request.data.get("user_id")
    topic_id = request.data.get("topic_id")
    info = Subscribers.objects.filter(user__id=user_id,
                                      topic__id=topic_id).first()
    user = Users.objects.get(pk=user_id)
    topic = Topics.objects.get(pk=topic_id)
    if info is None:
        subscriber = Subscribers.objects.create(user=user,
                                                topic=topic)
        return Response(subscriber.id)
    else:
        info.delete()
        return Response(0)


@api_view(['GET'])
def searchTopic(request, search_content):
    info = Topics.objects.filter(content__icontains=f'{search_content}')
    list_topic_id = []
    if info is None:
        return Response({"message": "no matching content found"})
    else:
        for data in info:
            topic_data = {"topic_id": data.id,
                          "topic_content": data.content}
            list_topic_id.append(topic_data)
        return Response(list_topic_id)


class CommentUpdate(generics.UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = UpdateCommentSerializer


class ListComment(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentCreation(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


@api_view(['POST'])
def likeComment(request):
    user_id = request.data.get("user_id")
    topic_id = request.data.get("topic_id")
    comment_id = request.data.get("comment_id")
    info = IsLikedComment.objects.filter(user__id=user_id,
                                         topic__id=topic_id,
                                         comment_id=comment_id).first()
    user = Users.objects.get(pk=user_id)
    topic = Topics.objects.get(pk=topic_id)
    comment = Comment.objects.get(pk=comment_id)
    if info is None:
        liker = IsLikedComment.objects.create(user=user,
                                              topic=topic,
                                              comment=comment)
        return Response(liker.id)
    else:
        info.delete()
        return Response(0)
