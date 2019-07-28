from django.shortcuts import render , redirect
from .forms import OuwnRegistrator
from django.contrib import messages


def register(request):
    if request.method == "POST":
        form = OuwnRegistrator(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'User {username} was successfully registered')
            return redirect ('blog')
    else:
        form = OuwnRegistrator()
    return render (request, 'hostes/main.html',{'form': form, 'title': 'Registration' })
