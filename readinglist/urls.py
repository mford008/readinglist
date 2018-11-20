from django.contrib import admin
from django.urls import path
from modifylist import views
# from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='homepage'),
    path('signup/', views.signup, name='signup'),
    # path('login/', auth_views.login, name='login'),
    # path('login/', views.login, name='login'),
    # path('logout/', auth_views.logout, name='logout'),
    path('dashboard/', views.dashboard),
]
