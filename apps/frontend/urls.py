from django.urls import path

from . import views

app_name = "organizations"

urlpatterns = [
    path('', views.index, name='index'),
]
