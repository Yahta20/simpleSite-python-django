from django.shortcuts import render , redirect
from .forms import OuwnRegistrator
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import OuwnRegistrator, UserUpdateForm, ProfileImage

def register(request):
    if request.method == "POST":
        form = OuwnRegistrator(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'User {username} was successfully registered. You can login.')
            return redirect ('login')
    else:
        form = OuwnRegistrator()
    return render (request, 'hostes/main.html',{'form': form, 'title': 'Registration' })


@login_required
def profile(request):
    if request.method == "POST":
            img_profile = ProfileImage(request.POST, request.FILES , instance = request.user.profile)
            update_user = UserUpdateForm(request.POST, instance = request.user)
            if update_user.is_valid() and img_profile.is_valid():
                update_user.save()
                img_profile.save()
                messages.success(request, f'You was successfully update profile.')
                return redirect('profile')

    else:
        img_profile = ProfileImage(instance = request.user.profile)
        update_user = UserUpdateForm(instance = request.user)
    data = {
        'img_profile'   :   img_profile,
        'update_user'   :   update_user
        }

    return render (request, 'hostes/profile.html', data)
