from django.contrib import admin

from foro.models import Thread, Comment


# Register your models here.

class ThreadAdmin(admin.ModelAdmin):
    list_display = ('title', 'creation_date')
    search_fields = ('title', 'content')
    date_hierarchy = 'creation_date'
    ordering = ('-creation_date',)


admin.site.register(Thread, ThreadAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('thread', 'creation_date')
    search_fields = ('thread', 'content')
    date_hierarchy = 'creation_date'
    ordering = ('-creation_date',)


admin.site.register(Comment, CommentAdmin)