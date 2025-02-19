from django.urls import path
from  . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("profile/<str:user_id>", views.user_profile, name="user-profile"),
    path('room/<str:pk>/', views.roomDetail, name='room-detail'),
    path('create-room/', views.createRoom, name='create-room'),
    path('update-room/<str:pk>/', views.updateRoom, name='update-room'),
    path('login/', views.loginPage, name='login'),
    path('delete/<str:pk>/', views.deleteRoom, name='delete-room'),
    path('delete-message/<str:pk>/', views.deleteMessage, name='delete-message'),
    path('edit-message/<str:pk>/', views.updateMessage, name='edit-message'),
    path('logout/', views.logoutPage, name='logout'),
    path('register/', views.registerPage, name='register')

]
