from django.urls import path
from knox import views as knox_views
from .views import UserAPIView, RegisterAPIView, LoginAPIView

urlpatterns = [
    path('login', LoginAPIView.as_view(), name='user-login'),
    path('logout', knox_views.LogoutView.as_view(), name='knox_logout'),
    path('logoutall', knox_views.LogoutAllView.as_view(), name='knox_logoutall'),
    path('register', RegisterAPIView.as_view(), name='user_register'),
    path('user', UserAPIView.as_view(), name='user_detail'),
]