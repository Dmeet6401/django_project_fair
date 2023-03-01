
from django.contrib import admin
from django.urls import path, include
from home import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.Index, name='home'),     # comes from home -> views.py -> function 
    path('about/', views.About, name='about'),
    path('login/', views.Login, name='login'),
    path('logout/', views.Logout, name='logout'),
    path('signup/', views.Signups, name='signup'),
    path('services/', views.Services, name='services'),
    path('contact/', views.Contacts, name='contact'),
    path('info/',views.Infos, name='info'),
    path('drone/', views.Drone ,name = 'drone'),
    path('admin/', admin.site.urls),
]
    