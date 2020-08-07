from django.contrib import admin
from posts.models import Post, Datt, User


admin.site.register(Post)
admin.site.register(Datt)

class UserAdmin(admin.ModelAdmin) :
    list_display = ('username', 'password')


admin.site.register(User, UserAdmin) #site에 등록