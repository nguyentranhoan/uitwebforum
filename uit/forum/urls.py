from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'forum'
urlpatterns = [
    path("test/test/<int:pk>/", views.TestTest.as_view()),
    path("dislike/", views.DislikeTopic),
    path("like/", views.IsLikedTopicCreate.as_view()),
    path("subscribe/", views.subsTopic),
    path("topic/<int:pk>/comment/", views.ListTopicComment.as_view()),
    path("user/list/", views.ListTopicComment.as_view()),
    path("comment/<int:pk>", views.CommentUpdate.as_view()),
    path("comment/", views.CommentCreation.as_view()),
    path("topic/list", views.ListTopic.as_view()),
    path("topic/create", views.createTopic),
    path("user/forgot/", views.forgot_password),
    path("user/<int:pk>/", views.UserInfo.as_view()),
    path("user/register/", views.register),
    path("user/login/", views.login),
    path("", views.home),
    # path("choices/", views.ChoiceList.as_view()),
    # path("choices/test/<int:pk>/", views.ChoiceDetail.as_view()),
    # path('questions/', views.QuestionListCreateAPIView.as_view()),
    path('api/api-auth', include('rest_framework.urls', namespace='rest-framework'))
]
