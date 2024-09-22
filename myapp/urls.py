from django.urls import path

from . import views


urlpatterns = [
    path("create_video/", views.create_video, name="create_video"),
    
]

