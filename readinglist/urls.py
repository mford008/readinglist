from django.contrib import admin
from django.urls import path
from modifylist import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage),
    path('signup/', views.signup),
    path('signin/', views.signin),
    path('dashboard/', views.dashboard),
]
