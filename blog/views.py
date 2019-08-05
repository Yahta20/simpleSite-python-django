from django.shortcuts import render
from .models import Post

def home (request):
    data = {
    'news' : Post.objects.all() ,
    'title':'Main page'
    }
    return render (request, 'blog/home.html',data)


def contacts (request):
    return render (request, 'blog/contacts.html',{'title':'Our contacts'})
