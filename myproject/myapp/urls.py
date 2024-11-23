from django.urls import path
from . import views
urlpatterns = [
    path('hello/', views.HelloWorldView.as_view()),
    path('users/', views.CreateUserView.as_view()),
    path('users/<str:username>/', views.GetUserView.as_view()),
    path('user/all/', views.GetAllUsersView.as_view()),
    path('users/<str:username>/update/', views.UpdateUserView.as_view()),
    path('users/<str:username>/delete/', views.DeleteUserView.as_view()),
]