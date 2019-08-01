from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

def home (request):
    data = {
    'news' : Post.objects.all(),
    'title':'Main page'
    }
    return render (request, 'blog/home.html',data)

class ShowNewsView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'news'
    ordering =['-date']

    def get_context_data(self, **kwards):
        ctx = super(ShowNewsView, self).get_context_data(**kwards)
        ctx['title'] = 'Main page'
        return ctx

class ShowNewsDetailView(DetailView):
    model = Post


def contacts (request):
    return render (request, 'blog/contacts.html',{'title':'Our contacts'})
