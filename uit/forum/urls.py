from django.urls import path, include

from . import views

app_name = 'forum'
urlpatterns = [
    path("like/", views.likeTopic),
    path("subscribe/", views.subsTopic),
    path("comment/<int:pk>", views.CommentUpdate.as_view()),
    path("comment/", views.CommentCreation.as_view()),
    path("topic/<int:topic_id>/views/count", views.increaseTopicView),
    path("topic/<int:topic_id>/views/", views.countNumberOfViews),
    path("topic/<int:topic_id>/subscribers/", views.countNumberOfSubscribers),
    path("topic/<int:topic_id>/likes/", views.countNumberOfLikes),
    path("topic/<int:topic_id>/comment/", views.listTopicComment),
    path("topic/list", views.ListTopic.as_view()),
    path("topic/create", views.createTopic),
    path("user/<int:pk>/info/", views.UserTotalInfo.as_view()),
    path("user/list/", views.ListUser.as_view()),
    path("user/password/reset", views.forgot_password),
    path("user/<int:pk>/", views.UserInfo.as_view()),
    path("user/register/", views.register),
    path("user/login/", views.login),
    path("", views.home),
    path('api/api-auth', include('rest_framework.urls', namespace='rest-framework'))
]
