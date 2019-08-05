from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):

    title   =   models.CharField(max_length=50)
    text    =   models.TextField()
    date    =   models.DateTimeField(default = timezone.now)
    autor   =   models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse ('blog_detail', kwargs = {'pk' : self.pk})
