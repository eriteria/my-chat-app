from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm


# Create your views here.
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


def profile(request):
    return render(request, 'account/profile.html')