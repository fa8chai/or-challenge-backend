from django.urls import include, path
from . import views

urlpatterns = [
    path('signup/', views.api_signup),
    path('signin/', views.api_login),
]