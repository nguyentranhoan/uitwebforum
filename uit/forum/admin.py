from django.contrib import admin
from .models import Users, Subscribers, Topics, Comment

# Register your models here.
admin.site.register(Users)
admin.site.register(Topics)
admin.site.register(Comment)
admin.site.register(Subscribers)
