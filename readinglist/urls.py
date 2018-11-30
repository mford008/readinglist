from django.contrib import admin
from django.urls import path
from modifylist import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='homepage'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/<username>', views.dashboard, name="dashboard"),
    path('delete_book/<book_id>', views.delete_book, name="delete_book")
]
