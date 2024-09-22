from django.contrib import admin
from .models import VideoRequest
# Register your models here.
@admin.register(VideoRequest)
class VideoRequestAdmin(admin.ModelAdmin):
    list_display = ('message', 'duration', 'width', 'height', 'file_name', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('message',)