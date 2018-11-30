from django.contrib import admin
from django.urls import path
from modifylist import views
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='homepage'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    # path('dashboard/', views.dashboard, name="dashboard"),
    path('dashboard/<username>/', views.dashboard, name="dashboard"),
]


# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
