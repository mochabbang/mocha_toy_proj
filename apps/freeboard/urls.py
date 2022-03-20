from django.urls import path, include
from apps.freeboard.views import views

urlpatterns = [
    path('', views.show_trasaction_list, name='transactions')
]