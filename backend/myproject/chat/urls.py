from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("<str:user_id>/", views.chat, name="chat"),
    path("<str:room_name>/", views.room, name="room"),

]