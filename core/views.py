from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import SignUpForm
from room.models import Room, Message


# Create your views here.
def front_page(request):
    recents = Message.objects.filter(user=request.user).order_by('-date_added')[:4]
    # recents =
    user_rooms = request.user.rooms.all()


    return render(request, 'core/frontpage.html', {'recents': recents, 'unread': user_rooms})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            user = form.save()
            print(user)
            login(request, user)
            return redirect('frontpage')
        else:
            print(form.errors)
            return render(request, 'core/signup.html', {'form': form})
    else:
        form = SignUpForm()

    return render(request, 'core/signup.html', {'form': form})



