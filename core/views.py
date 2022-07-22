from django.contrib.auth import login
from django.shortcuts import render, redirect
from room.models import Room, Message


# Create your views here.
def front_page(request):
    if request.user.is_authenticated:
        recents = Message.objects.filter(user=request.user).order_by('-date_added')[:4]
        # recents =
        user_rooms = request.user.rooms.all()
        return render(request, 'core/frontpage.html', {'recents': recents, 'unread': user_rooms})
    else:
        public_rooms = Room.objects.filter(visibility='public')
        return render(request, 'core/frontpage.html', {'rooms': public_rooms})







