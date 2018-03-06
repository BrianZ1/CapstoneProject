from django.contrib import admin

from .models import Comment
# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    fields = ['name', 'email', 'comment']
    list_display = ('name', 'email', 'comment')
    search_fields = ['name']

admin.site.register(Comment, CommentAdmin)