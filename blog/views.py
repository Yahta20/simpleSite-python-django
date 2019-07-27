from django.shortcuts import render
from django.http import HttpResponse

news  = [

    {
        'title' :   'First post',
        'text'  :   'Big time fat text',
        'date'  :   'today',
        'autor' :   'Rook',
    }
    ,
    {
        'title' :   'Second post',
        'text'  :   'Big time fart text',
        'date'  :   'today',

    }
]

# Create your views here.
def home (request):
    data = {
    'news' : news ,
    'title':'Main page'
    }

    return render (request, 'blog/home.html',data)


def contacts (request):
    return render (request, 'blog/contacts.html',{'title':'Our contacts'})
