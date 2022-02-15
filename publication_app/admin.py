from django.contrib import admin

from .models import Post


@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    list_display = ('id', 'create_date', 'title')
    ordering = ('-create_date', '-id', )
    readonly_fields = ('create_date',)
