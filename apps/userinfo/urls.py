from django.urls import path
from apps.userinfo.views import views

app_name = 'userinfo'

urlpatterns = [
    path('', views.login, name='login'),
]