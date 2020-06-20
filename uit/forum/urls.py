from django.urls import path, include

from . import views


app_name = 'forum'
urlpatterns = [
    path("api/search/<search_content>", views.searchTopic),
    path("api/like/", views.likeTopic),
    path("api/subscribe/", views.subsTopic),
    path("api/comment/<int:pk>", views.CommentUpdate.as_view()),
    path("api/comment/", views.CommentCreation.as_view()),
    path("api/topic/<int:pk>/", views.TopicInfo.as_view()),
    path("api/topic/<int:topic_id>/views/count", views.increaseTopicView),
    path("api/topic/<int:topic_id>/views/", views.countNumberOfViews),
    path("api/topic/<int:topic_id>/subscribers/", views.countNumberOfSubscribers),
    path("api/topic/<int:topic_id>/likes/", views.countNumberOfLikes),
    path("api/topic/<int:topic_id>/comment/", views.listTopicComment),
    path("api/topic/list", views.ListTopic.as_view()),
    path("api/topic/create", views.createTopic),
    path("api/category/", views.ListCategory.as_view()),
    path("api/user/<int:pk>/info/", views.UserTotalInfo.as_view()),
    path("api/user/list/", views.ListUser.as_view()),
    path("api/user/password/reset", views.forgot_password),
    path("api/user/<int:pk>/", views.UserInfo.as_view()),
    path("api/user/register/", views.register),
    path("api/user/login/", views.login),
    path("api/", views.home),
    path('api/api-auth', include('rest_framework.urls', namespace='rest-framework'))
]
