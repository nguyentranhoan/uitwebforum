from django.contrib import admin
from .models import Users, Categories, Subscribers, Topics, SubCategories, Comment

# Register your models here.
admin.site.register(Categories)
admin.site.register(SubCategories)
admin.site.register(Users)
admin.site.register(Topics)
admin.site.register(Comment)
admin.site.register(Subscribers)
