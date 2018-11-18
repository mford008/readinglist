from django.contrib import admin
from django.urls import path
from modifylist import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage)
]
