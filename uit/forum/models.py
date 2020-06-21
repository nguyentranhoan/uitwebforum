# Create your models here.

from django.db import models
from django.utils import timezone


class Users(models.Model):
    class Meta:
        db_table = 'users'

    username = models.CharField(max_length=200, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20)
    avatar = models.ImageField(default='images/ava.png')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.username


class UserAuth(models.Model):
    class Meta:
        db_table = 'user_auth'

    username = models.CharField(max_length=200, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20)
    created_at = models.DateTimeField(default=timezone.now)


# class Categories(models.Model):
#     class Meta:
#         db_table = 'categories'
#
#     name = models.CharField(max_length=200, unique=True)
#     is_active = models.BooleanField(default=True)
#     created_at = models.DateTimeField(default=timezone.now)
#
#     def __str__(self):
#         return self.name
#
#
# class SubCategories(models.Model):
#     class Meta:
#         db_table = 'sub_categories'
#
#     name = models.CharField(max_length=200)
#     category = models.ForeignKey(Categories, related_name='sub_cat', on_delete=models.CASCADE)
#     is_active = models.BooleanField(default=True)
#     created_at = models.DateTimeField(default=timezone.now)
#
#     def __str__(self):
#         return self.name


class Categories(models.Model):
    class Meta:
        db_table = 'categories'

    name = models.CharField(max_length=200, unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    parent = models.ForeignKey('Categories', related_name='sub_cat', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name


class Topics(models.Model):
    class Meta:
        db_table = 'topics'
    title = models.TextField(default="I have a question.")
    content = models.TextField()
    user = models.ForeignKey(Users, related_name='user_topic', on_delete=models.CASCADE)
    # sub_cat = models.ForeignKey(SubCategories, related_name='sub_cat_topic', on_delete=models.CASCADE)
    category = models.ForeignKey(Categories, related_name='category_topic', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Subscribers(models.Model):
    class Meta:
        db_table = 'subscribers'

    user = models.ForeignKey(Users, related_name='user_subscriber', on_delete=models.CASCADE)
    topic = models.ForeignKey(Topics, related_name='topic_subscriber', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user, self.topic


class IsLikedTopic(models.Model):
    class Meta:
        db_table = 'is_liked_topic'

    user = models.ForeignKey(Users, related_name='user_likes_topic', on_delete=models.CASCADE)
    topic = models.ForeignKey(Topics, related_name='topic_is_liked', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user, self.topic


class Comment(models.Model):
    class Meta:
        db_table = 'comment'

    content = models.TextField()
    user = models.ForeignKey(Users, related_name='user_comment', on_delete=models.CASCADE)
    topic = models.ForeignKey(Topics, related_name='topic_comment', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.content


class IsLikedComment(models.Model):
    class Meta:
        db_table = 'is_liked_comment'

    user = models.ForeignKey(Users, related_name='user_likes_comment', on_delete=models.CASCADE)
    topic = models.ForeignKey(Topics, related_name='topic_is_commented', on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, related_name='comment_is_liked', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user, self.topic, self.comment


class TopicStatistic(models.Model):
    class Meta:
        db_table = 'topic_statistic'

    topic = models.ForeignKey(Topics, related_name='topic_stat', on_delete=models.CASCADE)
    views = models.BigIntegerField(default=1)
    created_at = models.DateTimeField(default=timezone.now)
