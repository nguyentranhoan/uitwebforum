from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets

from .models import Users, Topics, Comment, Subscribers
from .serializers import QuestionSerializer, UserSerializer, TopicSerializer, CommentSerializer, SubscriberSerializer
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
    info = Users.objects.filter(usernam=username, password=password).first()
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


class TopicInfo(generics.ListCreateAPIView):
    queryset = Topics .objects.all()
    serializer_class = TopicSerializer


class CommentCreation(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class SubscriberInfo(generics.CreateAPIView):
    queryset = Subscribers.objects.all()
    serializer_class = SubscriberSerializer
#
#
# class QuestionViewSet(viewsets.ModelViewSet):
#     # queryset = Result.objects.raw("""select
#     #                                     polls_question.question_text,
#     #                                     polls_question.id,
#     #                                     result.point
#     #                                 from
#     #                                     result join polls_question
#     #                                     on result.question_id = polls_question.id
#     #                                 where
#     #                                     polls_question.id =1""")
#     queryset = Question.objects.all()
#     serializer_class = QuestionSerializer
#     # qr = Result.objects.raw("select * from result join question on result.question = question.id where question.id =1")
#
#

#
#
# class QuestionListCreateAPIView(APIView):
#
#     def get(self, request):
#         articles = models.Question.objects.all()
#         serializer = serializers.QuestionSerializer(articles, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = serializers.QuestionSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class ChoiceList(generics.ListCreateAPIView):
#     queryset = Choice.objects.order_by('id')[0:5]
#     serializer_class = ChoiceSerializer
#
#
# class ChoiceDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Choice.objects.all()
#     serializer_class = ChoiceSerializer
#
#
# class Login(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
