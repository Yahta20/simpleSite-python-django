from django.contrib import admin
from django.urls import path, include
#from django.conf.urls import url, include
from hostes import views as Hostv
from django.contrib.auth import views as authViews
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls'), name='blog'),
    path('reg/', Hostv.register, name = 'reg'),
    path('profile/', Hostv.profile, name = 'profile'),
    path('login/', authViews.LoginView.as_view(template_name='hostes/user.html'), name = 'login'),
    path('exit/', authViews.LogoutView.as_view(template_name='hostes/exit.html'), name = 'exit'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
