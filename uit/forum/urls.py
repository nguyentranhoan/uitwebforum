from django.urls import path, include

from . import views


app_name = 'forum'
urlpatterns = [
    path("api/comment/<comment_id>/likes/", views.countNumberOfLikesComment),
    path("api/comment/liked/", views.likeComment),
    path("api/comment/<int:pk>/update/", views.CommentUpdate.as_view()),
    path("api/comment/create/", views.CommentCreation.as_view()),
    path("api/comment/list/", views.ListComment.as_view()),
    path("api/topic/search/<search_content>/", views.searchTopic),
    path("api/topic/subscribed/", views.subsTopic),
    path("api/topic/liked/", views.likeTopic),
    path("api/topic/<int:topic_id>/views/count/", views.increaseTopicView),
    path("api/topic/<int:topic_id>/views/", views.countNumberOfViews),
    path("api/topic/<int:topic_id>/subscribers/", views.countNumberOfSubscribersTopic),
    path("api/topic/<int:topic_id>/likes/", views.countNumberOfLikesTopic),
    path("api/topic/<int:topic_id>/comment/", views.listTopicComment),
    path("api/topic/list/", views.ListTopic.as_view()),
    path("api/topic/<int:pk>/update/", views.UpdateTopic.as_view()),
    path("api/topic/create/", views.CreateTopic.as_view()),
    path("api/category/list/", views.ListCategory.as_view()),
    path("api/user/<user_id>/topic/<topic_id>/liked/comment/<comment_id>/check/", views.CheckUserLikedComment),
    path("api/user/<user_id>/liked/topic/<topic_id>/check/", views.CheckUserLikedTopic),
    path("api/user/<int:pk>/info/", views.UserTotalInfo.as_view()),
    path("api/user/list/", views.ListUser.as_view()),
    path("api/user/password/reset/", views.forgot_password),
    path("api/user/<int:pk>/update/", views.UpdateUserInfo.as_view()),
    path("api/user/register/", views.register),
    path("api/user/login/", views.login),
    path("api/", views.home),
    path('api/api-auth/', include('rest_framework.urls', namespace='rest-framework'))
]
