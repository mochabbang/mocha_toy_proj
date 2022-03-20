from django.urls import path
from apps.userinfo.views import views

urlpatterns = [
    path('', views.login, name='login'),
]