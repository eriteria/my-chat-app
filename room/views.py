from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404

from .forms import CreateRoomForm, EditRoomForm
from .models import Room, Message


# Create your views here.

@login_required
def rooms(request):
    rooms = Room.objects.all()
    return render(request, 'room/rooms.html', {'rooms': rooms})


@login_required
def create_room(request):
    form = CreateRoomForm()
    if request.method == 'POST':
        form = CreateRoomForm(request.POST)
        if form.is_valid():
            room = form.save(commit=True)
            room.creator = request.user
            room.members.add(request.user)
            room.save()
            return redirect('rooms')
        else:
            print(form.errors)

    return render(request, 'room/create_room.html', {'form': form})


@login_required
def room(request, slug):
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)[0:25]
    if request.user not in room.members.all():
        room.members.add(request.user)
    else:
        pass
    return render(request, 'room/room.html', {'room': room, 'messages': messages, 'location': 'room'})


@login_required
def leave_room(request, slug):
    room = Room.objects.get(slug=slug)
    if request.user in room.members.all():
        room.members.remove(request.user)
    else:
        pass
    return redirect('frontpage')


@login_required
def join_room(request, slug=None):
    try:
        room = Room.objects.get(slug=slug)
    except Exception:
        return redirect('rooms')
    if room:
        room.members.add(request.user)
        return redirect('room', slug)
    else:
        return redirect('rooms')


@login_required
def edit_room(request, slug):
    room = get_object_or_404(Room, slug=slug)

    form = EditRoomForm(instance=room)
    if request.user.id != room.creator.id:
        return HttpResponseForbidden()
    if request.method == 'POST':
        form = EditRoomForm(instance=room, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('frontpage')
        else:
            form = EditRoomForm(instance=room)
    return render(request, 'room/edit_room.html', {'form': form, 'room': room})


@login_required
def delete_room(request, slug):
    Room.objects.get(slug=slug).delete()
    return redirect('rooms')

