from django.urls import path

from . import views

urlpatterns = [
    path('', views.rooms, name='rooms'),
    path('create_room/', views.create_room, name='create_room'),
    path('leave_room/<slug:slug>', views.leave_room, name='leave_room'),
    path('join-room/', views.join_room),
    path('join-room/<slug:slug>', views.join_room, name='join_room'),
    path('edit-room/<slug:slug>', views.edit_room, name='edit_room'),
    path('delete-room/<slug:slug>', views.delete_room, name='delete_room'),
    path('<slug:slug>/', views.room, name='room'),
    ]