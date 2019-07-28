from django.contrib import admin
from django.urls import path, include
#from django.conf.urls import url, include
from hostes import views as Hostv


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls') ),
    path('reg/', Hostv.register, name = 'reg'),
]
