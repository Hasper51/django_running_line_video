from django.urls import path

from . import views


urlpatterns = [
    path("myapp/", views.video_text, name="video_text"),
    
]

