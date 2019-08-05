from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    )
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post

def home (request):
    data = {
    'news' : Post.objects.all() ,
    'title':'Main page'
    }
    return render (request, 'blog/home.html',data)

class ShowPostView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name  = 'news'
    ordering = ['-date']

    def get_context_data(self, **kwards):
        ctx = super(ShowPostView, self).get_context_data(**kwards)
        ctx ['title'] = 'Main page'
        return ctx

class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwards):
        ctx = super(PostDetailView, self).get_context_data(**kwards)
        ctx['title'] = Post.objects.filter(pk=self.kwargs['pk']).first()
        return ctx

class CreatePostView(LoginRequiredMixin,CreateView):
    model = Post
    fields = [
        'title',
        'text'
    ]
    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class UpdatePostView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = [
        'title',
        'text'
    ]
    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

    def test_func(self):
        news = self.get_object()
        if self.request.user == news.autor :
            return True
        return False

class DeletePostView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post

    success_url = '/'

    def test_func(self):
        news = self.get_object()
        if self.request.user == news.autor :
            return True
        return False

def contacts (request):
    return render (request, 'blog/contacts.html',{'title':'Our contacts'})
