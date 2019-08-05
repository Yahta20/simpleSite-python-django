from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.contrib.auth import login, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import default_token_generator
from django.http import HttpResponse
from django.shortcuts import render , redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .forms import OuwnRegistrator, UserUpdateForm, ProfileImage



def register(request):
    if request.method == "POST":
        form = OuwnRegistrator(request.POST)
        if form.is_valid():
            #form.save()
            #username = form.cleaned_data.get('username')
            #messages.success(request, f'User {username} was successfully registered. You can login.')
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':default_token_generator.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            print ('uid '+urlsafe_base64_encode(force_bytes(user.pk))+

            '\ntoken '+ default_token_generator.make_token(user))

            messages.success(request, f'{user} chek your email and activate account.')
            return redirect ('blog')
    else:
        form = OuwnRegistrator()
    return render (request, 'hostes/main.html',{'form': form, 'title': 'Registration' })

def activate(request, uidb64, token,backend='django.contrib.auth.backends.ModelBackend'):
    #try:
    print ("-activate-")
    uid = force_text(urlsafe_base64_decode(uidb64))
    user = User.objects.get(pk=uid)
    #except(TypeError, ValueError, OverflowError, User.DoesNotExist):
    #    user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect ('profile')
    else:
        messages.success(request, f'Chek your email and activate account.')
        return redirect('blog')


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
