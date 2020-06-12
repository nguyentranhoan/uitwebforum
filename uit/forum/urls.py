from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'forum'
urlpatterns = [
    path("subscribe/liked", views.LikedTopic),
    path("subscribe/", views.SubsTopic),
    path("comment/<int:pk>", views.CommentUpdate.as_view()),
    path("comment/", views.CommentCreation.as_view()),
    path("topic/", views.TopicInfo.as_view()),
    path("forgot/", views.forgot_password),
    path("user/<int:pk>/", views.UserInfo.as_view()),
    path("register/", views.register),
    path("login/", views.login),
    path("", views.home),
    # path("choices/", views.ChoiceList.as_view()),
    # path("choices/test/<int:pk>/", views.ChoiceDetail.as_view()),
    # path('questions/', views.QuestionListCreateAPIView.as_view()),
    path('api/api-auth', include('rest_framework.urls', namespace='rest-framework'))
]
