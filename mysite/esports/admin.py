from django.contrib import admin

from .models import Comment, Player, Event
# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    fields = ['name', 'email', 'comment']
    list_display = ('name', 'email', 'comment')
    search_fields = ['name']
    
class PlayerAdmin(admin.ModelAdmin):
    fields = ['name', 'count']
    list_display = ('name', 'count')
    search_fields = ['name']
    
class EventAdmin(admin.ModelAdmin):
    fields = ['name', 'count']
    list_display = ('name', 'count')
    search_fields = ['name']

admin.site.register(Comment, CommentAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(Event, EventAdmin)